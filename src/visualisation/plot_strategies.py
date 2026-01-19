from analysis.model_strategy import regime_strategy_returns
import matplotlib.pyplot as plt


def plot_strategies(model_col):
    df = regime_strategy_returns(model_col=model_col)

    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['strategy_cum_return'], label='returns')
    plt.plot(df.index, df['Close'], label='Buy and Hold')
    plt.title(f'{model_col} Strategy Returns')
    plt.xlabel("Date")
    plt.ylabel(f"Return Price")
    plt.legend()
    plt.tight_layout()
    plt.show()


plot_strategies(model_col="regime_kmeans")
plot_strategies(model_col="regime_gmm")
plot_strategies(model_col="regime_hmm")
