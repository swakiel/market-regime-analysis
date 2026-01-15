import pandas as pd
from constants import SYMBOLS, VOL_WINDOWS
from paths import PROCESSED_DATA_DIR, RAW_DATA_DIR


# MA dist and return/vol ratio
def add_trend_features(data):
    data = data.copy()

    # distance from moving average
    data["ma_50"] = data["Close"].rolling(50).mean()
    data["ma_dist_50"] = (data["Close"] - data["ma_50"]) / data["ma_50"]

    data["return_vol_ratio"] = data["log_return"] / data["vol_20"]

    data = data.set_index("Date").sort_index()
    data.dropna()

    print(data.tail())
    data.to_csv(f"{PROCESSED_DATA_DIR}/{symbol}_data_with_trend_features.csv")
    print(f"Data saved to {PROCESSED_DATA_DIR}/{symbol}_data.csv")


if __name__ == "__main__":
    for symbol in SYMBOLS:
        df = pd.read_csv(f"{PROCESSED_DATA_DIR}/{symbol}_data_with_basic_features.csv")
        add_trend_features(df)

