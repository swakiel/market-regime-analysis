from sklearn.mixture import GaussianMixture


class GMMRegimeModel:
    def __init__(self, n_regimes=3, random_state=42):
        self.model = GaussianMixture(
            n_components=n_regimes,
            covariance_type="full",
            random_state=random_state,
            n_init=10,
        )

    def fit(self, X):
        self.model.fit(X)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
