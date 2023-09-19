from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify,  request
from flask_debugtoolbar import DebugToolbarExtension
import yfinance as yf

import requests

app = Flask(__name__)

# Configure Flask Debug Toolbar
app.config['DEBUG_TB_ENABLED'] = True
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
toolbar = DebugToolbarExtension(app)


# def get_parsed_news(tickers, n):
#     # Define the URL for Finviz
#     finviz_url = 'https://finviz.com/quote.ashx?t='
#     news_tables = {}
#     # Loop through each ticker to fetch news data
#     for ticker in tickers:
#         url = finviz_url + ticker
#
#         # Make a request to the URL
#         req = Request(url=url, headers={'user-agent': 'sentiment-app'})
#         response = urlopen(req)
#         html = BeautifulSoup(response, features='html.parser')
#
#         # Find the news table
#         news_table = html.find(id='news-table')
#         news_tables[ticker] = news_table
#
#     parsed_news = []
#
#     # Loop through news tables and extract relevant information
#     for ticker, news_table in news_tables.items():
#         for row in news_table.findAll('tr'):
#             anchor_tag = row.a
#             time_data = row.td.text.strip().split()
#
#             if anchor_tag and len(time_data) >= 2:
#                 date, time = time_data[0], time_data[1]
#                 title = anchor_tag.get_text()
#                 parsed_news.append([ticker, date, time, title])
#     return parsed_news

# @app.route('/news')
# def news():
#     stock_symbols = "GOOG"  # Replace with the desired stock symbols
#     news_data = get_parsed_news(stock_symbols, 15)
#     return render_template('news.html', news=news_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
    return render_template('home.html')

# Function to scrape data from the API and parse it using Beautiful Soup
# Function to scrape data from the API and parse it using Beautiful Soup
def scrape_news():
    url = 'https://api.apilayer.com/financelayer/news?date=today&keywords=at%26t&sources=seekingalpha.com&keyword=merger&tickers=dis'
    headers = {'apikey': 'TaRvTlocSJ6Pjjb8VxsQQah1Hc9ZMwqH'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('data', [])
        # Limit the number of articles to 15
        return articles[:25]
    else:
        return None

@app.route('/news')
def news():
    scraped_data = scrape_news()
    return render_template('news.html', news_data=scraped_data)


@app.route('/indicator')
def indicators():
    return render_template('indicator.html')

@app.route('/crypto')
def crypto():
    API_KEY = "79514ef0-0e2e-4e7b-9474-66f8154975f0"
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    params = {
        "start": "1",
        "limit": "25",  # Change this limit as needed
        "convert": "USD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    cryptocurrencies = data.get("data")
    return render_template('crypto.html', cryptocurrencies=cryptocurrencies)

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/arima')
def arima():
    return render_template('arima.html')

@app.route('/lstm')
def lstm():
    return render_template('lstm.html')

@app.route('/linear_regression')
def linear_regression():
    return render_template('linear_regression.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
