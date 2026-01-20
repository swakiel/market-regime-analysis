import yfinance as yf
import pandas as pd
from constants import SYMBOLS
from paths import RAW_DATA_DIR


def fetch_stock_data(symbols=SYMBOLS, start_date="2005-01-01", end_date="2025-12-31"):
    for ticker_symbol in symbols:
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
                continue

            data.to_csv(f"{RAW_DATA_DIR}/{ticker_symbol}_data_raw.csv")
            print(f"Data saved to {RAW_DATA_DIR}/{ticker_symbol}_data_raw.csv")


        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    return None


if __name__ == "__main__":
    fetch_stock_data()
