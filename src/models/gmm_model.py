from sklearn.mixture import GaussianMixture
from models.base import RegimeModel


class GMMRegimeModel(RegimeModel):
    def fit(self, X):
        self.model = GaussianMixture(
            n_components=self.n_regimes,
            covariance_type="full",
            random_state=self.random_state,
            n_init=10,
        )
        self.model.fit(X)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
