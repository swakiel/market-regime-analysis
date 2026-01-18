import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.cluster import KMeans


class HMMRegimeModel:
    def __init__(
        self,
        n_regimes=3,
        random_state=42,
        covariance_type="full",
        n_iter=300,
        tol=1e-3,
    ):
        self.n_regimes = n_regimes
        self.random_state = random_state

        # HMM configuration
        self.model = GaussianHMM(
            n_components=n_regimes,
            covariance_type=covariance_type,
            n_iter=n_iter,
            tol=tol,
            init_params="",
            random_state=random_state,
        )

    def fit(self, X):
        X = np.asarray(X)

        # Initialize means, covariances, transitions, starting probabilities
        self._initialize_with_kmeans(X)
        self._initialize_transitions()
        self._initialize_startprob()

        self.model.fit(X)

        return self

    # ---------------------------------------------------------
    # INITIALIZATION HELPERS
    # ---------------------------------------------------------
    def _initialize_with_kmeans(self, X):
        """
        Use KMeans to initialize means for stability.
        """
        kmeans = KMeans(
            n_clusters=self.n_regimes,
            random_state=self.random_state,
            n_init=20,
        ).fit(X)

        # Means
        self.model.means_ = kmeans.cluster_centers_

        # Covariances (diagonal or full depending on model config)
        cov = np.cov(X, rowvar=False)
        eps = 1e-3
        cov += eps * np.eye(cov.shape[0])

        if self.model.covariance_type == "diag":
            diag_cov = np.diag(np.diag(cov))
            self.model.covars_ = np.tile(np.diag(diag_cov), (self.n_regimes, 1))
        else:
            self.model.covars_ = np.tile(cov, (self.n_regimes, 1, 1))

    def _initialize_transitions(self):
        """
        Initialize a persistent transition matrix.
        """
        P = np.full((self.n_regimes, self.n_regimes),
                    0.10 / (self.n_regimes - 1))
        np.fill_diagonal(P, 0.90)
        self.model.transmat_ = P

    def _initialize_startprob(self):
        """
        Uniform starting probabilities.
        """
        self.model.startprob_ = np.full(self.n_regimes, 1.0 / self.n_regimes)

    def predict(self, X):
        X = np.asarray(X)
        return self.model.predict(X)

    def predict_proba(self, X):
        X = np.asarray(X)
        return self.model.predict_proba(X)

    def transition_matrix(self):
        return self.model.transmat_