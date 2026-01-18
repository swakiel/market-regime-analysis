import matplotlib.pyplot as plt
from models.run_models import run_all_models


def plot_gmm_probabilities():
    df = run_all_models(n_regimes=3)

    plt.figure(figsize=(14, 5))
    for i in range(3):
        plt.plot(df.index, df[f"gmm_prob_{i}"], label=f"Regime {i}")

    plt.title("GMM Regime Probabilities")
    plt.ylabel("Probability")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_gmm_probabilities()