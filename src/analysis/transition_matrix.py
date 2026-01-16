import pandas as pd
import numpy as np

from models.run_models import run_all_models


def compute_transition_matrix(regime_series):
    """
    Computes regime transition probability matrix
    """
    transitions = pd.crosstab(
        regime_series.shift(1),
        regime_series,
        normalize="index",
    )

    return transitions


def get_transition_matrices():
    df = run_all_models(n_regimes=3)

    matrices = {}

    for model_col in ["regime_kmeans", "regime_gmm"]:
        matrices[model_col] = compute_transition_matrix(df[model_col])

    return matrices


if __name__ == "__main__":
    matrices = get_transition_matrices()

    for model, matrix in matrices.items():
        print(f"\nTransition Matrix: {model}\n")
        print(matrix.round(3))
