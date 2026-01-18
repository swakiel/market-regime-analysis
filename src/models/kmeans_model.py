from sklearn.cluster import KMeans


class KMeansRegimeModel:
    def __init__(self, n_regimes=3, random_state=42):
        self.model = KMeans(
            n_clusters=n_regimes,
            random_state=random_state,
            n_init=20
        )

    def fit(self, X):
        self.model.fit(X)
        return self

    def predict(self, X):
        return self.model.predict(X)
