from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

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

# amzn_data = news_tables["AMZN"]
key = next(iter(news_tables))
amzn_data = news_tables[key]
amzn_rows = amzn_data.findAll('tr')
print(amzn_rows)

for index, html in enumerate(amzn_rows):
 if isinstance(html, str):
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <tr> elements
    table_rows = soup.find_all('tr')

    for row in table_rows:
        # Find the <a> tag within the <div> with class "news-link-left"
        anchor_tag = row.find('div', class_='news-link-left').find('a')
        if anchor_tag:
            print("Text:", anchor_tag.text.strip())
            print("URL:", anchor_tag['href'])



# for ticker, news_table in news_tables.items():
#
#     for row in news_table.findAll('tr'):
#
#         # Check if 'a' element exists within the row
#         if row.a:
#
#             title = row.a.text
#             date_data = row.td.text.split(' ')
#
#             if len(date_data) == 1:
#                 time = date_data[0]
#             else:
#                 date = date_data[0]
#                 time = date_data[1]
#
#                 # Check if the 'date' string is not empty or invalid
#                 if date.strip():
#                     parsed_data.append([ticker, date, time, title])
#
# df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
#
# # Convert the 'date' column to datetime, handling empty or invalid date strings
# df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
#
# # Remove rows with invalid dates (NaT)
# df = df.dropna(subset=['date'])
#
# vader = SentimentIntensityAnalyzer()
#
# f = lambda title: vader.polarity_scores(title)['compound']
# df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'] if title else 0)
#
# # Convert the 'date' column to datetime, handling empty or invalid date strings
# df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
#
# # Remove rows with invalid dates (NaT)
# df = df.dropna(subset=['date'])
#
# plt.figure(figsize=(10,8))
# mean_df = df.groupby(['ticker', 'date']).mean().unstack()
# mean_df = mean_df.xs('compound', axis="columns")
# mean_df.plot(kind='bar')
# plt.show()