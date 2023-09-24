import pandas as pd
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import matplotlib.pyplot as plt
import pickle

class StockSentimentClassifier:
    def __init__(self,ticker):
        self.vader = SentimentIntensityAnalyzer()
        self.ticker = ticker

    def get_stock_data(self, ticker):
        current_date = datetime.now().strftime("%Y-%m-%d")
        finviz_url = 'https://finviz.com/quote.ashx?t='

        news_tables = {}

        url = finviz_url + ticker
        req = Request(url=url, headers={'user-agent': 'my-app'})
        response = urlopen(req)
        html = BeautifulSoup(response, features='html.parser')
        news_table = html.find(id='news-table')
        news_tables[ticker] = news_table

        key = ticker
        stock_data = news_tables[key]
        stock_rows = stock_data.findAll('tr')
        parsed_data = []
        prev_date = None
        for index, row in enumerate(stock_rows):
            title_ = row.a
            if title_:
                title = title_.text
            timestamp_ = row.td
            if timestamp_:
                timestamp = timestamp_.text
                date_data = [data.strip() for data in timestamp.split(" ") if data.strip()]
                if len(date_data) == 1:
                    time = date_data[0]
                    date = prev_date
                else:
                    date = date_data[0]
                    if date != "Today":
                        date = datetime.strptime(date_data[0], "%b-%d-%y").strftime("%Y-%m-%d")
                        prev_date = date
                    else:
                        date = current_date
                        prev_date = current_date
                    time = date_data[1]

            parsed_data.append([key, date, time, title])

        df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
        df['compound'] = df['title'].apply(lambda title: self.vader.polarity_scores(title)['compound'] if title else 0)
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
        df["time"] = df["time"].str.replace("AM", "").str.replace("PM", "")

        return df

    def plot_sentiment(self, ticker):
        df = self.get_stock_data(ticker)
        plt.figure(figsize=(10, 8))
        df['compound'] = pd.to_numeric(df['compound'], errors='coerce')
        mean_df = df.groupby(['ticker', 'date'])['compound'].mean().unstack()
        mean_df.plot(kind='bar')
        return df, plt

    def save_sentiment_model(self, filename='sentiment_model.pkl'):
        # Save the sentiment analysis model to a pickle file
        with open(filename, 'wb') as model_file:
            pickle.dump(self.vader, model_file)


