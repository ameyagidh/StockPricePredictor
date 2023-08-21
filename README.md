# Stock Market Prediction Project

## Project Description

The goal of this project is to develop and evaluate various machine learning models for predicting stock market movements using a combination of historical time series data and sentiment analysis from news articles. The project aims to explore different approaches to improve the accuracy of predictions and backtest strategies against benchmark results.

The project focuses on six FTSE 100 companies: AstraZeneca, GlaxoSmithKline, BP, Royal Dutch Shell, HSBC, and Unilever. These companies represent diverse sectors such as oil, pharmaceuticals, finance, and consumer goods.

## Table of Contents
1. [Exploratory Data Analysis](#exploratory-data-analysis)
2. [Technical Analysis](#technical-analysis)
3. [Time Series Forecasting](#time-series-forecasting)
4. [Sentiment Analysis](#sentiment-analysis)
5. [Algorithm Selection and Training](#algorithm-selection-and-training)
6. [Data Sources](#data-sources)
7. [Python Libraries](#python-libraries)
8. [Project Structure](#project-structure)
9. [Getting Started](#getting-started)
10. [Conclusion](#conclusion)

## Exploratory Data Analysis<a name="exploratory-data-analysis"></a>

The project begins with exploring historical stock data using the yfinance API. It involves downloading and analyzing opening price, highest and lowest prices, closing price, trading volume, and adjusted close price. The adjusted close price, accounting for stock splits and dividends, will be used for prediction.

## Technical Analysis<a name="technical-analysis"></a>

The technical analysis section employs various indicators like Moving Averages, MACD, Stochastic Oscillator, RSI, and more. These indicators are used to identify trading signals and patterns. The goal is to explore different technical strategies to enhance prediction accuracy.

## Time Series Forecasting<a name="time-series-forecasting"></a>

Time series models are crucial for predicting stock trends. The project covers the process of transforming non-stationary data into stationary form using differencing. Different time series models like ARIMA, SARIMA, and Facebook Prophet are evaluated. Additionally, RNN models like LSTM and GRU are explored for deeper analysis.

## Sentiment Analysis<a name="sentiment-analysis"></a>

News articles from Investing.com are collected using web scraping tools like Selenium and Beautiful Soup. Sentiment analysis using NLP tools like VADER and TextBlob is performed on these articles. The sentiment scores are then combined with historical stock data to assess their impact on stock price movement.

## Algorithm Selection and Training<a name="algorithm-selection-and-training"></a>

The project tackles both regression and classification problems for stock prediction. Various machine learning models will be used, including Gaussian Naive Bayes, Gradient Boosting, and more. A detailed evaluation of each model's performance using confusion matrices is conducted.

## Data Sources<a name="data-sources"></a>

The primary data sources for this project are Yahoo! Finance for historical stock data and Investing.com for news articles. The combination of these datasets helps build accurate prediction models.

## Python Libraries<a name="python-libraries"></a>

The project utilizes a wide range of Python libraries for data manipulation, visualization, machine learning, and natural language processing. Some of the key libraries include NumPy, Pandas, Matplotlib, Seaborn, Plotly, SciPy, Statsmodels, Scikit-learn, Keras, TensorFlow, Beautiful Soup, Selenium, NLTK, TextBlob, SpaCy, Gensim, BERT, Hugging Face, and PyTorch.

## Project Structure<a name="project-structure"></a>

The project follows a structured approach:

1. **Exploratory Data Analysis**: Understand the historical stock data.
2. **Technical Analysis**: Apply various technical indicators and strategies.
3. **Time Series Forecasting**: Build and evaluate time series models.
4. **Sentiment Analysis**: Collect and analyze news article sentiments.
5. **Algorithm Selection and Training**: Choose and train ML models.
6. **Conclusion**: Summarize findings and insights.

## Getting Started<a name="getting-started"></a>

To run the project, follow these steps:

1. Install required Python libraries using `pip install -r requirements.txt`.
2. Execute the Python scripts in the respective project sections.

## Conclusion<a name="conclusion"></a>

The Stock Market Prediction project explores a holistic approach to predicting stock market movements using a combination of technical analysis, time series forecasting, and sentiment analysis. By leveraging historical data and NLP techniques, the project aims to develop accurate prediction models that can aid in making informed trading decisions.

The detailed analysis and thorough evaluation of different strategies and models provide insights into the complexities of stock market prediction and demonstrate the potential of combining multiple approaches for improved accuracy.
