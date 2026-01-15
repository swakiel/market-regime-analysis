import pandas as pd
from constants import SYMBOLS, VOL_WINDOWS, BASE
from paths import PROCESSED_DATA_DIR, ANALYSIS_DIR


def expanding_zscore(series):
    mean = series.expanding(min_periods=max(VOL_WINDOWS)).mean()
    std = series.expanding(min_periods=max(VOL_WINDOWS)).std()
    return (series - mean) / std


def normalise_datasets(symbols=SYMBOLS, windows=VOL_WINDOWS):
    for symbol in symbols:
        df = pd.read_csv(
            f"{PROCESSED_DATA_DIR}/{symbol}_data_with_trend_features.csv",
            parse_dates=["Date"],
            index_col="Date"
        )

        df["log_return"] = expanding_zscore(df["log_return"])
        df["ma_dist_50"] = expanding_zscore(df["ma_dist_50"])

        for window in windows:
            df[f"vol_{window}"] = expanding_zscore(df[f"vol_{window}"])

        df = df.dropna()
        df.to_csv(f"{PROCESSED_DATA_DIR}/{symbol}_NORMAL.csv")


def normalise_correlations(symbols=SYMBOLS, windows=VOL_WINDOWS, base=BASE):
    df = pd.read_csv(
        f"{ANALYSIS_DIR}/correlations.csv",
        parse_dates=["Date"],
        index_col="Date"
    )
    for symbol in symbols:
        if symbol == base:
            continue

        for window in windows:
            column = f"corr_{base.lower()}_{symbol.lower()}_{window}"
            df[column] = expanding_zscore(df[column])

    df = df.dropna()
    df.to_csv(f"{ANALYSIS_DIR}/correlations_NORMAL.csv")


if __name__ == "__main__":
    normalise_datasets()
    normalise_correlations()