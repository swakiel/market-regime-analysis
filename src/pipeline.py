"""
End-to-end pipeline for market regime detection.

This script orchestrates:
1. Data loading
2. Feature engineering
3. Regime model fitting
4. Evaluation and visualisation
"""

from data.yahoo_data import fetch_stock_data
from features.basic_features import add_basic_features
from features.correlation import correlations
from features.trend_features import add_trend_features
from features.normilisation import normalise_correlations, normalise_datasets
from analysis.regime_stats import compute_regime_stats
from visualisation.plot_volatility import plot_volatility
from visualisation.plot_regimes import plot_price_with_labeled_regimes
from visualisation.plot_strategies import plot_strategies
from constants import MODELS


def run_pipeline(n_regimes=3):
    print("Sourcing data...")
    fetch_stock_data()

    print("\nAdding features and normalise...")
    add_basic_features()
    correlations()
    add_trend_features()
    normalise_correlations()
    normalise_datasets()

    plot_volatility()

    print("\nFitting regime models and computing regime statistics...")
    for model in MODELS:
        stats = compute_regime_stats(f"regime_{model}")
        print(f"\n{model.upper()} REGIME STATS")
        print(stats.round(4))

    print("\nPlotting regimes...")
    for model in MODELS:
        plot_price_with_labeled_regimes(model)

    print("\nEvaluating strategies...")
    for model in MODELS:
        plot_strategies(model=model)

    print("\n✅ Pipeline completed.")


if __name__ == "__main__":
    run_pipeline(n_regimes=3)
