import pandas as pd
import matplotlib.pyplot as plt
from constants import BASE, VOL_WINDOWS
from paths import ANALYSIS_DIR, FIGURE_DIR


def plot_correlation(windows=VOL_WINDOWS, base=BASE):

    df = pd.read_csv(
        f"{ANALYSIS_DIR}/correlations.csv",
        parse_dates=["Date"],
        index_col="Date"
    )

    plt.figure(figsize=(12, 6))

    for window in windows:
        for col in df.columns:
            if col.startswith(f"corr_{base.lower()}") and col.endswith(f"_{window}"):
                plt.plot(df[col], label=col.replace("corr_", "").upper())

        plt.axhline(0, linewidth=1)

        plt.title(f"Rolling {window}-Day Correlations with {base.upper()}")
        plt.xlabel("Date")
        plt.ylabel("Correlation")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{FIGURE_DIR}/{window}-day_correlations.png", bbox_inches="tight")
        plt.show()


if __name__ == "__main__":
    plot_correlation()
