def label_regimes(stats_df):
    """
    Assign economic labels based on volatility
    """
    ordered = stats_df.sort_values("Volatility").index.tolist()

    return {
        ordered[0]: "Calm / Growth",
        ordered[1]: "Transition",
        ordered[2]: "Stress / Crisis",
    }