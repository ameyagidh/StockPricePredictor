# Stock Market Prediction Project

## Project Description

The goal of this project is to develop and evaluate various machine learning models for predicting stock market movements using a combination of historical time series data and sentiment analysis from news articles. The project aims to explore different approaches to improve the accuracy of predictions and backtest strategies against benchmark results.

Real Time StockMarket Data Storage is done on AWS Athena using AWS Glue Crawler, I used an S3 bucket and an EC2 instance to configure this using Apache kafka and zookeeper
link to Dynamic Storage repository :- https://github.com/ameyagidh/MarketWatchDog


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
2. **Time Series Forecasting**: Build and evaluate time series models.
3. **Sentiment Analysis**: Collect and analyze news article sentiments.
4. **Algorithm Selection and Training**: Choose and train ML models.
5. **Conclusion**: Summarize findings and insights.

## Getting Started<a name="getting-started"></a>

To run the project, follow these steps:

1. Install required Python libraries using `pip install -r requirements.txt`.
2. Execute the Python scripts in the respective project sections.

## Conclusion<a name="conclusion"></a>

The Stock Market Prediction project explores a holistic approach to predicting stock market movements using a combination of technical analysis, time series forecasting, and sentiment analysis. By leveraging historical data and NLP techniques, the project aims to develop accurate prediction models that can aid in making informed trading decisions.

The detailed analysis and thorough evaluation of different strategies and models provide insights into the complexities of stock market prediction and demonstrate the potential of combining multiple approaches for improved accuracy.


## Screenshots

<img width="1496" alt="Screenshot 2023-09-26 at 2 24 03 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/61e4e3af-7407-4289-866e-86c1b32824bc">
<img width="1496" alt="Screenshot 2023-09-26 at 2 24 14 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/0945efbd-b4b8-468a-bcb3-7ea031d674e5">
<img width="1496" alt="Screenshot 2023-09-26 at 2 27 19 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/7e3958fa-8fe3-47a2-9029-2efca82e9329">
<img width="1496" alt="Screenshot 2023-09-26 at 2 25 12 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/f1266e5e-e8ee-43eb-b5ab-d053fe3ace6d">
<img width="1496" alt="Screenshot 2023-09-26 at 2 25 51 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/8df50371-df22-4f7d-915d-0b9a1f84a60f">
<img width="1496" alt="Screenshot 2023-09-26 at 2 25 55 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/77b38868-2b5a-42db-86a4-582e572c1851">
<img width="1496" alt="Screenshot 2023-09-26 at 2 26 05 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/6689b5dd-2942-4b4b-9cb1-7229bcfc8ce9">
<img width="1496" alt="Screenshot 2023-09-19 at 3 53 41 PM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/5c8f0e9f-1c20-4494-a5aa-8d68b5020b62">
<img width="1496" alt="Screenshot 2023-09-26 at 2 27 05 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/21a2e9c4-8402-4df6-bc91-d32fd2bd92cc">
<img width="739" alt="LSTM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/b6f5ffb5-fb19-42ea-8f7b-b41139839883">
<img width="720" alt="Screenshot 2023-09-26 at 2 33 54 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/5377c425-c55e-49ed-ac7c-0d4e658f7f89">
<img width="567" alt="Screenshot 2023-09-26 at 2 34 37 AM" src="https://github.com/ameyagidh/StockPricePredictor/assets/65457905/177ac7ea-40ec-48fe-93f4-d13d2f7ff9fe">

## Bitcoin Predictions
### Transformers
![image1](https://github.com/ameyagidh/StockPricePredictor/assets/65457905/32d06a9f-c2ba-43c5-b4be-7128fa07dc13)

### ARIMA
![image7](https://github.com/ameyagidh/StockPricePredictor/assets/65457905/aaa22e32-fcaa-4e9a-98a4-7236d2da0cf1)

### Moving Average
![image4](https://github.com/ameyagidh/StockPricePredictor/assets/65457905/230c0500-cc83-479f-9576-806459812498)

### Ensemble Model
![image8](https://github.com/ameyagidh/StockPricePredictor/assets/65457905/dfd24a31-6f6f-4e50-b9cb-a1e070a392e7)

In the context of stock price prediction, advanced models struggle to capture nonlinear patterns in historical data. However, applying a basic moving average (window size = 10) improves predictions, especially in capturing both upward and downward trends, although it still faces issues with outliers.

The ARIMA model performs well when prices are relatively stable but falters with significant price fluctuations, making it better suited for short-term rather than long-term predictions.

The CNN model's performance on testing data is modest due to its simplicity. However, when combined with the Transformer model and moving averages, a Linear Regression model outperforms all others, including ARIMA, achieving an impressive R2 score of 0.9535. This suggests that the CNN and Moving Averages models capture complementary features for price prediction.

## References
https://www.investing.com/equities/

https://finance.yahoo.com/quote/API/

