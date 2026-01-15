import pandas as pd
import matplotlib.pyplot as plt
from constants import SYMBOLS, CRISIS_DATES
from paths import PROCESSED_DATA_DIR, FIGURE_DIR


def plot_return_volatility_ratio(symbols=SYMBOLS):
    for symbol in symbols:
        df = pd.read_csv(
            f"{PROCESSED_DATA_DIR}/{symbol}_data_with_trend_features.csv",
            parse_dates=["Date"],
            index_col="Date"
        )

        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df["return_vol_ratio"], label="Return/Volatility Ratio")

        for label, date in CRISIS_DATES.items():
            plt.axvline(pd.to_datetime(date), linestyle="--")

        plt.title(f"{symbol} Return/Volatility Ratio")
        plt.xlabel("Date")
        plt.ylabel("R/V")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{FIGURE_DIR}/{symbol}_Return_Vol_ratio.png", bbox_inches="tight")

        plt.show()


if __name__ == "__main__":
    plot_return_volatility_ratio()