from analysis.model_strategy import regime_strategy_returns
import matplotlib.pyplot as plt


def plot_strategies(model):
    df = regime_strategy_returns(model=model)

    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['strategy_equity'], label='Strategy returns')
    plt.plot(df.index, df['bh_equity'], label='Buy and Hold')
    plt.title(f'{model.upper()} Strategy Returns')
    plt.xlabel("Date")
    plt.ylabel(f"Portfolio Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_strategies(model="kmeans")
    plot_strategies(model="gmm")
    plot_strategies(model="hmm")
