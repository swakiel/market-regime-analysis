import pandas as pd
import numpy as np
from models.run_models import run_all_models
from paths import PROCESSED_DATA_DIR
from constants import BASE
from analysis.regime_stats import compute_regime_stats
from analysis.regime_utils import label_regimes


def regime_strategy_returns(model_col):
    """
    Compute daily strategy returns based on regime labels.

    Strategy:
    - Calm / Growth    -> Long (+1)
    - Stress / Crisis  -> Short (-1)
    - Transition       -> Hold previous position
    """

    df = run_all_models(n_regimes=3)

    prices = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/{BASE}_data_with_trend_features.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = df.join(prices["Close"], how="inner")

    stats = compute_regime_stats(model_col)
    label_map = label_regimes(stats)

    df["return"] = df["Close"].pct_change()

    data = df.copy()

    data["regime_label"] = data[model_col].map(label_map)

    # Initialise position column
    position = np.zeros(len(data))
    prev_position = 0
    first_purchase_price = 0

    for i, regime in enumerate(data["regime_label"]):
        if regime == "Calm / Growth":
            prev_position = 1
            if first_purchase_price == 0:
                first_purchase_price = data["Close"][i]
        elif regime == "Stress / Crisis":
            prev_position = -1
        elif regime == "Transition":
            pass  # hold previous position
        else:
            raise ValueError(f"Unknown regime label: {regime}")

        position[i] = prev_position

    data["position"] = position
    data["strategy_return"] = data["position"].shift(1) * data["return"]
    data["strategy_cum_return"] = (1 + data["strategy_return"]).cumprod() - 1
    data["strategy_cum_return"] = data["strategy_cum_return"] * first_purchase_price

    data = data.dropna()

    return data

if __name__ == "__main__":
    data = regime_strategy_returns(model_col="regime_kmeans")
    data = regime_strategy_returns(model_col="regime_kmeans")
    data = regime_strategy_returns(model_col="regime_kmeans")