from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify,  request
from flask_debugtoolbar import DebugToolbarExtension
import yfinance as yf
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import requests
from Models.SentimentAnalysis.stocksentiment import StockSentimentClassifier


app = Flask(__name__)

# Configure Flask Debug Toolbar
app.config['DEBUG_TB_ENABLED'] = True
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
toolbar = DebugToolbarExtension(app)


def get_index_data(symbol):
    try:
        # Fetch data for the specified symbol (e.g., "^GSPC" for S&P 500, "^IXIC" for NASDAQ)
        data_ind = yf.download(symbol, period="1d", interval="1d")
        # Round numerical columns to 2 decimal places
        data_ind['Open'] = data_ind['Open'].round(2)
        data_ind['High'] = data_ind['High'].round(2)
        data_ind['Low'] = data_ind['Low'].round(2)
        data_ind['Close'] = data_ind['Close'].round(2)
        data_ind['Volume'] = data_ind['Volume'].round(2)
        return data_ind.to_html(classes="table table-bordered")
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
@app.route('/home')
def home():
    sp500_data = get_index_data("^GSPC")
    # Get NASDAQ index data
    nasdaq_data = get_index_data("^IXIC")

    top_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA','NVDA']

    # Initialize an empty list to store stock data
    stock_data = []

    # Fetch data for each top stock
    for stock_symbol in top_stocks:
        stock = yf.Ticker(stock_symbol)
        stock_info = {
            'symbol': stock_symbol,
            'name': stock.info.get('longName', ''),
            'price': round(stock.history(period="1d")['Close'].iloc[-1], 2),
            'change': round(stock.history(period="1d")['Close'].iloc[-1] - stock.history(period="1d")['Open'].iloc[0],
                            2),
             'logo_filename': f'{stock_symbol}.png',
        }
        stock_data.append(stock_info)

    return render_template('home.html', sp500_data=sp500_data, nasdaq_data=nasdaq_data, stock_data=stock_data)


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

def technicalIndicator(indi, data):
    if indi == "Moving Average":
        period_ma = 15
        data[f'{period_ma} Day MA'] = data['Close'].rolling(window=period_ma).mean()
    elif indi == "RSI":
        period_rsi = 15
        delta = data['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period_rsi).mean()
        avg_loss = loss.rolling(window=period_rsi).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        data['RSI'] = rsi

@app.route('/indicator')
def indicators():
    return render_template('indicator.html')

n_years = 20
period = n_years * 365

@app.route('/results', methods=['POST'])
def results():
    # Get the selected stock symbol from the form
    stock_symbol = request.form.get('stock_symbol')

    try:
        data = yf.download(stock_symbol, period="1d", interval="1m", auto_adjust=True)
        data2 = data.iloc[25:36]
        technicalIndicator("Moving Average", data)  # Calculate Moving Average
        technicalIndicator("RSI", data)  # Calculate RSI

        # Calculate the moving average and RSI
        fifteen_day_ma = data['15 Day MA']
        rsi = data['RSI']
        # Create a Plotly figure for the Moving Average
        import plotly.express as px

        fig_ma = px.line(data_frame=data, x=data.index, y=fifteen_day_ma, title=f'15 Day MA for {stock_symbol}')
        fig_ma.update_xaxes(title='Date')
        fig_ma.update_yaxes(title='15 Day MA')

        # Convert the Moving Average plot to HTML
        plot_html = fig_ma.to_html()

        fig_rsi = px.line(data_frame=data, x=data.index, y=rsi, title=f'RSI for {stock_symbol}')
        fig_rsi.update_xaxes(title='Date')
        fig_rsi.update_yaxes(title='RSI')

        # Convert the RSI plot to HTML
        rsi_plot_html = fig_rsi.to_html()

        # Predict the output data
        data.reset_index(inplace=True)
        data["Datetime"] = data["Datetime"].dt.tz_localize(None)
        df_train = data[['Datetime', 'Close']].rename(columns={"Datetime": "ds", "Close": "y"})
        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)
        print(forecast)

        fig_forecast = plot_plotly(m, forecast)

        # Convert the Prophet forecast plot to HTML
        forecast_plot_html = fig_forecast.to_html()

        return render_template('indicator.html', data=data2.to_html(), stock_symbol=stock_symbol,
                               plot_html=plot_html, rsi_plot_html=rsi_plot_html, forecast_plot_html=forecast_plot_html)
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template('indicator.html', error_message=error_message)

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


@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    return render_template('sentiment.html', sentiment_df=None, plot_filename=None)

@app.route('/resultsentiment', methods=['POST'])
def resultssentiment():
    stock_symbol = request.form.get('stock_symbol')
    # Use the StockSentimentClassifier to perform sentiment analysis
    classifier = StockSentimentClassifier(stock_symbol)
    df = classifier.get_stock_data(stock_symbol)
    print(df)
    # Pass the sentiment data and plot filename to the template
    return render_template('sentiment.html',stock_symbol = stock_symbol,sentiment_df =df[:15])


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
