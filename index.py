import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Example: Fetching stock data for Apple (AAPL)
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2023-01-01"

data = fetch_stock_data(ticker, start_date, end_date)

# Step 2: Calculate moving averages
data['50-Day MA'] = data['Close'].rolling(window=50).mean()
data['200-Day MA'] = data['Close'].rolling(window=200).mean()

# Step 3: Calculate daily returns
data['Daily Return (%)'] = data['Close'].pct_change() * 100

# Step 4: Calculate volatility (standard deviation of daily returns)
data['Volatility'] = data['Daily Return (%)'].rolling(window=30).std()

# Step 5: Plot the data
plt.figure(figsize=(14, 7))

# Plot Closing Price
plt.plot(data['Close'], label='Closing Price', color='blue', alpha=0.7)
# Plot Moving Averages
plt.plot(data['50-Day MA'], label='50-Day MA', color='orange', linestyle='--')
plt.plot(data['200-Day MA'], label='200-Day MA', color='green', linestyle='--')

# Add labels and title
plt.title(f'{ticker} Stock Price Analysis')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Step 6: Plot Daily Returns
plt.figure(figsize=(14, 7))
plt.plot(data['Daily Return (%)'], label='Daily Return (%)', color='purple')
plt.axhline(0, color='red', linestyle='--', alpha=0.6)
plt.title(f'{ticker} Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.legend()
plt.grid()
plt.show()

# Display the last 10 rows of the data
print(data.tail(10))
