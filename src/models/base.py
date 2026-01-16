class RegimeModel:
    def __init__(self, n_regimes, random_state=42):
        self.n_regimes = n_regimes
        self.random_state = random_state

    def fit(self, X):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError
