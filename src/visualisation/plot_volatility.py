import pandas as pd
import matplotlib.pyplot as plt
from constants import SYMBOLS, VOL_WINDOWS
from paths import PROCESSED_DATA_DIR, FIGURE_DIR


def plot_volatility(symbols=SYMBOLS, vol_windows=VOL_WINDOWS):
    for symbol in symbols:
        df = pd.read_csv(
            f"{PROCESSED_DATA_DIR}/{symbol}_data_with_features.csv",
            parse_dates=["Date"],
            index_col="Date"
        )

        plt.figure(figsize=(12, 6))
        for window in vol_windows:
            plt.plot(df.index, df[f"vol_{window}"], label=f"{window}-day volatility")
            #plt.plot(df.index, df["vol_60"], label="60-day volatility")

        plt.title(f"{symbol} Rolling Volatility")
        plt.xlabel("Date")
        plt.ylabel("Volatility")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{FIGURE_DIR}/{symbol}_volatility.png", bbox_inches="tight")

        plt.show()


if __name__ == "__main__":
    plot_volatility()