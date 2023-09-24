from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date in "YYYY-MM-DD" format
finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')

    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
    break

key = next(iter(news_tables))
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
        date_data = [data.strip() for data in timestamp.split(" ") if data.strip()]  # Remove empty strings
        # print(date_data)
        # print(len(date_data))
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

    parsed_data.append([key,date,time,title])

# print(parsed_data)

# df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
# vader = SentimentIntensityAnalyzer()
# df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'] if title else 0)
# print(df)

# # Convert the 'date' column to datetime, handling empty or invalid date strings
# df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

# Remove rows with invalid dates (NaT)
# df = df.dropna(subset=['date'])
# f = lambda title: vader.polarity_scores(title)['compound']
# # Convert the 'date' column to datetime, handling empty or invalid date strings
# df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

#Remove rows with invalid dates (NaT)
# df = df.dropna(subset=['date'])

# plt.figure(figsize=(10,8))
# mean_df = df.groupby(['ticker', 'date']).mean().unstack()
# mean_df = mean_df.xs('compound', axis="columns")
# mean_df.plot(kind='bar')
# plt.show()