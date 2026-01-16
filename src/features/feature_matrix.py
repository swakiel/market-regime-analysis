import pandas as pd
from  paths import ANALYSIS_DIR, PROCESSED_DATA_DIR


FEATURE_COLUMNS = [
    "vol_20",
    "vol_60",
    "ma_dist_50",
    "corr_spy_tlt_60",
    "corr_spy_gld_60",
]


def load_feature_matrix():
    """
    Build aligned feature matrix used by all regime models
    """

    spy = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/SPY_NORMAL.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    corr = pd.read_csv(
        f"{ANALYSIS_DIR}/correlations_NORMAL.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    df = pd.concat(
        [
            spy[["vol_20", "vol_60", "ma_dist_50"]],
            corr[["corr_spy_tlt_60", "corr_spy_gld_60"]],
        ],
        axis=1,
    ).dropna()

    return df