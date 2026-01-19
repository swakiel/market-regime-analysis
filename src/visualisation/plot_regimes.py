import pandas as pd
import matplotlib.pyplot as plt

from models.run_models import run_model
from analysis.regime_stats import compute_regime_stats
from analysis.regime_utils import label_regimes
from paths import PROCESSED_DATA_DIR, FIGURE_DIR
from constants import BASE, REGIME_COLOURS


def plot_price_with_labeled_regimes(model, n_regimes=3):
    df, _ = run_model(model_name=model, n_regimes=n_regimes)

    prices = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/{BASE}_data_with_trend_features.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = df.join(prices["Close"], how="inner")

    stats = compute_regime_stats(f"regime_{model}", df)
    label_map = label_regimes(stats)

    plt.figure(figsize=(14, 6))

    for regime, label in label_map.items():
        plt.plot(
            df.index,
            df["Close"].where(df[f"regime_{model}"] == regime),
            label=label,
            color=REGIME_COLOURS[label],
            linewidth=1.8,
        )

    plt.title(f"{BASE} Price with Market Regimes ({model.upper()})")
    plt.xlabel("Date")
    plt.ylabel(f"{BASE} Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        f"{FIGURE_DIR}/{model}_over_{BASE}_closing_prices.png",
        bbox_inches="tight",
    )
    plt.show()


if __name__ == "__main__":
    plot_price_with_labeled_regimes("kmeans")
    plot_price_with_labeled_regimes("gmm")
    plot_price_with_labeled_regimes("hmm")
