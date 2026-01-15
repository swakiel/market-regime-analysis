import pandas as pd
import numpy as np
from constants import SYMBOLS, VOL_WINDOWS


def add_features(data):
    data = data.copy()

    # day on day return
    data["log_return"] = np.log(data["Close"] / data["Close"].shift(1))

    #volatility over windows in VOL_WINDOWS
    for window in VOL_WINDOWS:
        data["vol_" + str(window)] = data["log_return"].rolling(window=window).std()

    data = data.set_index("Date").sort_index()

    return data.dropna()


if __name__ == "__main__":
    for symbol in SYMBOLS:
        df = pd.read_csv(f"../raw/{symbol}_data_raw.csv")
        df = add_features(df)

        if df is not None:
            print(df.head())
            df.to_csv(f"{symbol}_data_with_features.csv")
            print(f"Data saved to {symbol}_data.csv")