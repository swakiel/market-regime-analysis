import pandas as pd
import numpy as np
from models.run_models import run_model
from paths import PROCESSED_DATA_DIR
from constants import BASE
from analysis.regime_stats import compute_regime_stats
from analysis.regime_utils import label_regimes


def regime_strategy_returns(model):
    """
    Compute daily strategy returns based on regime labels.

    Strategy:
    - Calm / Growth    -> Long (+1)
    - Stress / Crisis  -> Short (-1)
    - Transition       -> Hold previous position
    """

    initial_capital = 10_000

    df, _ = run_model(model_name=model, n_regimes=3)

    prices = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/{BASE}_data_with_trend_features.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = df.join(prices["Close"], how="inner")

    stats = compute_regime_stats(f"regime_{model}", df)
    label_map = label_regimes(stats)

    df["return"] = df["Close"].pct_change()

    data = df.copy()

    data["regime_label"] = data[f"regime_{model}"].map(label_map)

    # Initialise position column
    position = np.zeros(len(data))
    prev_position = 0

    for i, regime in enumerate(data["regime_label"]):
        if regime == "Calm / Growth":
            prev_position = 1
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
    data["strategy_equity"] = initial_capital * (1 + data["strategy_return"]).cumprod()
    data["bh_equity"] = initial_capital * (1 + data["return"]).cumprod()

    data = data.dropna()

    return data

if __name__ == "__main__":
    data = regime_strategy_returns(model="kmeans")
    data = regime_strategy_returns(model="kmeans")
    data = regime_strategy_returns(model="kmeans")