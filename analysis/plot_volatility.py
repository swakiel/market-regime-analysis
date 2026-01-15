import pandas as pd
import matplotlib.pyplot as plt
from constants import SYMBOLS, VOL_WINDOWS

DATA_PATH = "../data/processed"

for symbol in SYMBOLS:
    df = pd.read_csv(
        f"{DATA_PATH}/{symbol}_data_with_features.csv",
        parse_dates=["Date"],
        index_col="Date"
    )

    plt.figure(figsize=(12, 6))
    for window in VOL_WINDOWS:
        plt.plot(df.index, df[f"vol_{window}"], label=f"{window}-day volatility")
        #plt.plot(df.index, df["vol_60"], label="60-day volatility")

    plt.title(f"{symbol} Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.tight_layout()

    plt.show()
