import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "correlations.csv",
    parse_dates=["Date"],
    index_col="Date"
)

plt.figure(figsize=(12, 6))

if "corr_spy_tlt" in df.columns:
    plt.plot(df.index, df["corr_spy_tlt"], label="SPY–TLT")

if "corr_spy_gld" in df.columns:
    plt.plot(df.index, df["corr_spy_gld"], label="SPY–GLD")

plt.axhline(0, linewidth=1)

plt.title("Rolling 60-Day Correlations with SPY")
plt.xlabel("Date")
plt.ylabel("Correlation")
plt.legend()
plt.tight_layout()

plt.show()
