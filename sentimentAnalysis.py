from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt


def get_parsed_news(tickers, n):
    # Define the URL for Finviz
    finviz_url = 'https://finviz.com/quote.ashx?t='

    news_tables = {}

    # Loop through each ticker to fetch news data
    for ticker in tickers:
        url = finviz_url + ticker

        # Make a request to the URL
        req = Request(url=url, headers={'user-agent': 'sentiment-app'})
        response = urlopen(req)
        html = BeautifulSoup(response, features='html.parser')

        # Find the news table
        news_table = html.find(id='news-table')
        news_tables[ticker] = news_table

    parsed_news = []

    # Loop through news tables and extract relevant information
    for ticker, news_table in news_tables.items():
        for row in news_table.findAll('tr'):
            anchor_tag = row.a
            time_data = row.td.text.strip().split()

            if anchor_tag and len(time_data) >= 2:
                date, time = time_data[0], time_data[1]
                title = anchor_tag.get_text()
                parsed_news.append([ticker, date, time, title])

    return parsed_news


# Define the list of tickers and number of recent news articles to retrieve
tickers = ['GOOG', 'AMZN', 'AAPL', 'MSFT', 'TSLA', 'NFLX', 'META', 'GME', 'PANW','BUD', 'WMT', 'W', 'NVDA']
n = 3

# Fetch parsed news data
parsed_news = get_parsed_news(tickers, n)

# Create DataFrame and calculate sentiment scores using VADER
vader = SentimentIntensityAnalyzer()
df = pd.DataFrame(parsed_news, columns=['ticker', 'date', 'time', 'title'])
df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'])
df['date'] = pd.to_datetime(df['date'])
print(df)
# Plotting mean sentiment scores
# plt.figure(figsize=(10, 8))
mean_df = df.groupby(['ticker', 'date'])['compound'].mean().unstack()
mean_df.plot(kind='bar')
plt.title('Mean Sentiment Score by Ticker and Date')
plt.xlabel('Date')
plt.ylabel('Mean Sentiment Score')
plt.legend(title='Ticker')
plt.show()