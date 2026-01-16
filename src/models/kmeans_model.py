from sklearn.cluster import KMeans
from models.base import RegimeModel


class KMeansRegimeModel(RegimeModel):
    def fit(self, X):
        self.model = KMeans(
            n_clusters=self.n_regimes,
            random_state=self.random_state,
            n_init=20,
        )
        self.model.fit(X)
        return self

    def predict(self, X):
        return self.model.predict(X)
