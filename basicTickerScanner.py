import yfinance as yf
import pandas as pd
from IPython.display import display

# Define the tickers you want to scan
index_tickers = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD',
                '^N225','^HSI','^GDAXI','^DJI','^GSPC']

# Function to calculate ATR (Average True Range)
def calculate_atr(data, period=14):
    high = data['High']
    low = data['Low']
    close = data['Close']

    tr = pd.DataFrame(index=data.index)
    tr['HL'] = high - low
    tr['HC'] = abs(high - close.shift())
    tr['LC'] = abs(low - close.shift())

    atr = tr.max(axis=1).rolling(window=period).mean()

    return atr

# Function to calculate SMA (Simple Moving Average)
def calculate_sma(data, period):
    return data['Close'].rolling(window=period).mean()

# Function to calculate RSI (Relative Strength Index)
def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

# Function to calculate the percentage difference between the closing price and SMA
def calculate_percentage_difference(closing_price, sma):
    return ((closing_price - sma) / sma) * 100

# Function to scan and compute values for each index and return a DataFrame
def scan_market_indexes(index_tickers):
    results = []

    for ticker in index_tickers:
        data = yf.download(ticker, period="1y")  # Download 1-year historical data

        atr = calculate_atr(data)
        sma20 = calculate_sma(data, 20)
        sma50 = calculate_sma(data, 50)
        sma200 = calculate_sma(data, 200)
        rsi = calculate_rsi(data)

        current_price = round(data['Close'].iloc[-1], 2)
        fifty_two_week_high = round(data['High'].max(), 2)
        fifty_two_week_low = round(data['Low'].min(), 2)
        price_change = round(current_price - data['Close'].iloc[-2], 2)
        volume = round(data['Volume'].iloc[-1], 2)

        result = {
            'Ticker': ticker,
            'ATR': round(atr.iloc[-1], 2),
            'SMA20': calculate_percentage_difference(current_price, sma20.iloc[-1]),
            'SMA50': calculate_percentage_difference(current_price, sma50.iloc[-1]),
            'SMA200': calculate_percentage_difference(current_price, sma200.iloc[-1]),
            'RSI': round(rsi.iloc[-1], 2),
            'Current_Price': current_price,
            '52_Week_High': fifty_two_week_high,
            '52_Week_Low': fifty_two_week_low,
            'Price_Change': price_change,
            'Volume': volume
        }

        results.append(result)

    return pd.DataFrame(results)

# Function to apply cell styling for price change and SMA percentage difference
def highlight_changes(val):
    if isinstance(val, str):
        val = float(val.replace('%', '').replace('(', '').replace(')', ''))
    color = 'background-color: green' if val > 0 else 'background-color: pink'
    return color

if __name__ == "__main__":
    market_df = scan_market_indexes(index_tickers)

    # Apply the price change and SMA percentage difference cell styling
    styled_market_df = market_df.style.applymap(highlight_changes, subset=['Price_Change', 'SMA20', 'SMA50', 'SMA200'])

    # Display the styled DataFrame
    display(styled_market_df)
