import pandas as pd
from constants import SYMBOLS, BASE, VOL_WINDOWS
from paths import PROCESSED_DATA_DIR, ANALYSIS_DIR

def correlations(symbols=SYMBOLS, windows=VOL_WINDOWS, base=BASE):
    dfs = {}

    for symbol in symbols:
        dfs[symbol] = pd.read_csv(
            f"{PROCESSED_DATA_DIR}/{symbol}_data_with_basic_features.csv",
            parse_dates=["Date"],
            index_col="Date"
        )

    returns = pd.concat(
        [dfs[s]["log_return"].rename(s) for s in symbols],
        axis=1
    ).dropna()

    for symbol in symbols:
        if symbol == base:
            continue

        for window in windows:
            returns[f"corr_{base.lower()}_{symbol.lower()}_{window}"] = (
                returns[base].rolling(window).corr(returns[symbol])
            )

    returns.to_csv(f"{ANALYSIS_DIR}/correlations.csv")



if __name__ == "__main__":
    correlations()

