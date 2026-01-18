import pandas as pd
import numpy as np

from models.run_models import run_all_models
from paths import PROCESSED_DATA_DIR
from constants import BASE


def max_drawdown(series):
    cumulative = (1 + series).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()


def average_regime_duration(regime_series):
    """
    Returns average duration (in days) spent in each regime
    """
    blocks = (
        regime_series
        .ne(regime_series.shift())
        .cumsum()
    )

    durations = (
        regime_series
        .groupby(blocks)
        .agg(["first", "size"])
        .rename(columns={"first": "regime", "size": "duration"})
    )

    return durations.groupby("regime")["duration"].mean()



def compute_regime_stats(model_col):
    df = run_all_models(n_regimes=3)

    prices = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/{BASE}_data_with_trend_features.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = df.join(prices[["Close"]], how="inner")

    # Daily returns from prices (not standardized)
    df["return"] = df["Close"].pct_change()
    df = df.dropna()

    stats = []

    avg_durations = average_regime_duration(df[model_col])

    for regime in sorted(df[model_col].unique()):
        subset = df[df[model_col] == regime]

        mean_return = subset["return"].mean()
        vol = subset["return"].std()
        sharpe = mean_return / vol if vol != 0 else np.nan
        mdd = max_drawdown(subset["return"])
        pct_time = len(subset) / len(df)

        stats.append(
            {
                "Regime": regime,
                "Mean Return": mean_return,
                "Volatility": vol,
                "Sharpe": sharpe,
                "Percentage Time": pct_time,
                "Max Drawdown": mdd,
                "Avg Regime Length (days)": avg_durations.loc[regime],
                "Observations": len(subset),
            }
        )

    pd.set_option("display.max_columns", None)
    return pd.DataFrame(stats).set_index("Regime")


if __name__ == "__main__":
    kmeans_stats = compute_regime_stats("regime_kmeans")
    gmm_stats = compute_regime_stats("regime_gmm")
    hmm_stats = compute_regime_stats("regime_hmm")

    print("\nKMeans Regime Stats\n")
    print(kmeans_stats.round(4))

    print("\nGMM Regime Stats\n")
    print(gmm_stats.round(4))

    print("\nHMM Regime Stats\n")
    print(hmm_stats.round(4))
