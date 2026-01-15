import pandas as pd
from constants import SYMBOLS

WINDOW = 60
dfs = {}

for symbol in SYMBOLS:
    dfs[symbol] = pd.read_csv(
        f"../data/processed/{symbol}_data_with_features.csv",
        parse_dates=["Date"],
        index_col="Date"
    )

returns = pd.concat(
    [dfs[s]["log_return"].rename(s) for s in SYMBOLS],
    axis=1
).dropna()


BASE = "SPY"

for symbol in SYMBOLS:
    if symbol == BASE:
        continue
    returns[f"corr_{BASE.lower()}_{symbol.lower()}"] = (
        returns[BASE].rolling(WINDOW).corr(returns[symbol])
    )



print(returns.tail())
returns.to_csv("correlations.csv")