import yfinance as yf
import pandas as pd
from constants import SYMBOLS


def fetch_stock_data(ticker_symbol, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.

    :param ticker_symbol: Stock ticker (e.g., 'AAPL', 'TSLA')
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: Pandas DataFrame with stock data or None if failed
    """
    try:
        # Validate date format
        pd.to_datetime(start_date)
        pd.to_datetime(end_date)

        # Create Ticker object
        ticker = yf.Ticker(ticker_symbol)

        # Download historical data
        data = ticker.history(start=start_date, end=end_date, auto_adjust=True)
        data = data[["Open", "High", "Low", "Close", "Volume"]]

        if data.empty:
            print(f"No data found for {ticker_symbol} in the given date range.")
            return None

        return data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == "__main__":
    start = "2004-01-01"
    end = "2025-12-31"

    for symbol in SYMBOLS:
        stock_data = fetch_stock_data(symbol, start, end)

        if stock_data is not None:
            print(stock_data.head())
            stock_data.to_csv(f"{symbol}_data_raw.csv")
            print(f"Data saved to {symbol}_data_raw.csv")
