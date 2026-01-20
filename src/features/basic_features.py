import pandas as pd
import numpy as np
from constants import SYMBOLS, VOL_WINDOWS
from paths import PROCESSED_DATA_DIR, RAW_DATA_DIR


# volatility and log returns
def add_basic_features(symbols=SYMBOLS, vol_window=VOL_WINDOWS):
    for symbol in symbols:
        data = pd.read_csv(f"{RAW_DATA_DIR}/{symbol}_data_raw.csv")
        data = data.copy()

        # day on day return
        data["log_return"] = np.log(data["Close"] / data["Close"].shift(1))

        #volatility over windows in vol_window
        for window in vol_window:
            data["vol_" + str(window)] = data["log_return"].rolling(window=window).std()

        data = data.set_index("Date").sort_index()
        data.dropna()

        data.to_csv(f"{PROCESSED_DATA_DIR}/{symbol}_data_with_basic_features.csv")
        print(f"Data saved to {PROCESSED_DATA_DIR}/{symbol}_data_with_basic_features.csv")


if __name__ == "__main__":
    add_basic_features()

