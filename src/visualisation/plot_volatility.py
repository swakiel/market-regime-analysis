import pandas as pd
import matplotlib.pyplot as plt
from constants import SYMBOLS, VOL_WINDOWS, CRISIS_DATES
from paths import PROCESSED_DATA_DIR, FIGURE_DIR


def plot_volatility(symbols=SYMBOLS, vol_windows=VOL_WINDOWS):
    for symbol in symbols:
        df = pd.read_csv(
            f"{PROCESSED_DATA_DIR}/{symbol}_data_with_trend_features.csv",
            parse_dates=["Date"],
            index_col="Date"
        )

        plt.figure(figsize=(12, 6))
        for window in vol_windows:
            plt.plot(df.index, df[f"vol_{window}"], label=f"{window}-day volatility")

        for label, date in CRISIS_DATES.items():
            plt.axvline(pd.to_datetime(date), linestyle="--")

        plt.title(f"{symbol} Rolling Volatility")
        plt.xlabel("Date")
        plt.ylabel("Volatility")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{FIGURE_DIR}/{symbol}_volatility.png", bbox_inches="tight")

        plt.show()


if __name__ == "__main__":
    plot_volatility()