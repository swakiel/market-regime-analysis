SYMBOLS = ["SPY", "TLT", "GLD"]
EQUITY = "SPY"
VOL_WINDOWS = [20, 60]
BASE = "SPY"
CRISIS_DATES = {
    "2008 Crisis": "2008-09-15",
    "COVID Crash": "2020-03-16",
}

REGIME_LABELS = {
    "low_vol": "Calm / Growth",
    "mid_vol": "Transition",
    "high_vol": "Stress / Crisis",
}

REGIME_COLOURS = {
        "Calm / Growth": "green",
        "Transition": "gold",
        "Stress / Crisis": "red",
}