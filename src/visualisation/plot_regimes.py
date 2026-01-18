import pandas as pd
import matplotlib.pyplot as plt

from models.run_models import run_all_models
from analysis.regime_stats import compute_regime_stats
from analysis.regime_utils import label_regimes
from paths import PROCESSED_DATA_DIR, FIGURE_DIR
from constants import BASE, REGIME_COLOURS


def plot_price_with_labeled_regimes(model_col, n_regimes=3):
    df = run_all_models(n_regimes=n_regimes)

    prices = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/{BASE}_data_with_trend_features.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = df.join(prices["Close"], how="inner")

    stats = compute_regime_stats(model_col)
    label_map = label_regimes(stats)

    plt.figure(figsize=(14, 6))

    for regime, label in label_map.items():
        plt.plot(
            df.index,
            df["Close"].where(df[model_col] == regime),
            label=label,
            color=REGIME_COLOURS[label],
            linewidth=1.8,
        )

    plt.title(f"{BASE} Price with Market Regimes ({model_col})")
    plt.xlabel("Date")
    plt.ylabel(f"{BASE} Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        f"{FIGURE_DIR}/{model_col}_over_{BASE}_closing_prices.png",
        bbox_inches="tight",
    )
    plt.show()


if __name__ == "__main__":
    plot_price_with_labeled_regimes("regime_kmeans")
    plot_price_with_labeled_regimes("regime_gmm")
