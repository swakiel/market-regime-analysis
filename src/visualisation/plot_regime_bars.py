import matplotlib.pyplot as plt
from paths import FIGURE_DIR
from analysis.regime_stats import compute_regime_stats
from analysis.regime_utils import label_regimes


def plot_regime_bars(model_col):
    stats = compute_regime_stats(model_col)

    labels = label_regimes(stats)
    stats = stats.rename(index=labels)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    stats["Sharpe"].plot(kind="bar", ax=axes[0], title="Sharpe Ratio")
    stats["Volatility"].plot(kind="bar", ax=axes[1], title="Volatility")
    stats["Max Drawdown"].plot(kind="bar", ax=axes[2], title="Max Drawdown")

    for ax in axes:
        ax.grid(True, alpha=0.3)

    plt.suptitle(f"Regime Statistics – {model_col}")
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/{model_col}_stats_bars.png", bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    plot_regime_bars("regime_kmeans")
    plot_regime_bars("regime_gmm")
