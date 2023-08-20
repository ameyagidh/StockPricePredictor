# Using Yahoo Finance data and Facebook Prophet for prediction

import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date

# Set page title and background color
st.set_page_config(page_title="Market Momentum App", page_icon="📈", layout="wide")

# Define colors for consistent styling
primary_color = "#1f77b4"  # Blue
secondary_color = "#d62728"  # Red
text_color = "#333333"  # Dark gray
background_color = "#f4f4f4"  # Light gray

# Set overall app style with gradient background
gradient_background_css = f"""
    body {{
        background: linear-gradient(to bottom, {primary_color}, {background_color});
        color: {text_color};
        font-family: 'Arial', sans-serif;
    }}
    .st-h1, .st-h2, .st-h3, .st-h4, .st-h5, .st-h6 {{
        color: {primary_color};
        font-weight: bold;
        text-shadow: 2px 2px {secondary_color};
    }}
    .stButton {{
        background-color: {primary_color};
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        box-shadow: 2px 2px {secondary_color};
    }}
    .stButton:hover {{
        background-color: {secondary_color};
    }}
    .stText, .stNumber {{
        color: {text_color};
        margin-bottom: 10px;
    }}
    .stMarkdown {{
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    .stInfoBox {{
        background-color: {background_color};
        border: 1px solid {primary_color};
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
    }}
    .stHeader {{
        background-color: {primary_color};
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }}
"""

# Apply custom CSS with gradient background
st.markdown(f"<style>{gradient_background_css}</style>", unsafe_allow_html=True)

st.sidebar.title("Stock Predictor")
st.sidebar.write("Select a stock or index for prediction:")
options = ('GOOG', 'PANW', 'AMZN', 'BUD', 'AAPL', 'MSFT', 'GME', 'TSLA', 'NFLX', 'META', 'WMT', 'W','NVDA')

selected_option = st.sidebar.selectbox('Select stock or index:', options)

n_years = st.sidebar.slider('Years of prediction:', 1, 13)
period = n_years * 365

# Load data and show loading status
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start="2010-01-01", end=date.today())
    data.reset_index(inplace=True)
    return data

data_load_state = st.sidebar.text('Loading data...')
data = load_data(selected_option)
data_load_state.text('Data loaded!')

# Main content area
st.title("Market Momentum Web App")
st.subheader(f"Forecast for {selected_option} Data")

# Display raw data in a table
st.subheader('Raw Data')
st.dataframe(data.head())

# Display interactive raw data plot
st.subheader('Raw Data Plot')
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Open", line=dict(color=primary_color)))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close", line=dict(color=secondary_color)))
fig.update_layout(title_text='Time Series Data', xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

# Predict forecast with Prophet
df_train = data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"})
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Display forecast plot
st.subheader(f'Forecast Plot for {n_years} Years')
fig1 = plot_plotly(m, forecast)
fig1.update_traces(line=dict(color=primary_color))
st.plotly_chart(fig1)

# Display forecast components
st.subheader('Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)

# Additional section: Technical Indicators
st.header("Technical Indicators")
selected_indicator = st.selectbox("Select a technical indicator:", ["Moving Average", "RSI"])

if selected_indicator == "Moving Average":
    period_ma = st.slider("Select the moving average period:", 5, 50, 20)
    data[f'{period_ma} Day MA'] = data['Close'].rolling(window=period_ma).mean()
    st.subheader(f"{period_ma}-Day Moving Average")
    st.line_chart(data[f'{period_ma} Day MA'])

elif selected_indicator == "RSI":
    period_rsi = st.slider("Select the RSI period:", 5, 50, 14)
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period_rsi).mean()
    avg_loss = loss.rolling(window=period_rsi).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    st.subheader("Relative Strength Index (RSI)")
    st.line_chart(data['RSI'])

# Additional section: Comparative Analysis
st.header("Comparative Analysis")
selected_comparisons = st.multiselect("Select stocks or indices for comparison:", options)
comparison_data = {}

if selected_comparisons:
    for comparison in selected_comparisons:
        comparison_data[comparison] = load_data(comparison)

    st.write("Comparison of Close Prices")
    comparison_fig = go.Figure()
    for comparison, comp_data in comparison_data.items():
        comparison_fig.add_trace(go.Scatter(x=comp_data['Date'], y=comp_data['Close'], name=comparison))
    comparison_fig.update_layout(title_text='Close Price Comparison', xaxis_rangeslider_visible=True)
    st.plotly_chart(comparison_fig)

# Additional section: Historical vs. Forecasted Comparison
st.header("Historical vs. Forecasted Comparison")

st.line_chart(data[['Date', 'Close']].set_index('Date'))
st.line_chart(forecast.set_index('ds'))
