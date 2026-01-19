from features.feature_matrix import load_feature_matrix
from models.kmeans_model import KMeansRegimeModel
from models.gmm_model import GMMRegimeModel
from models.hmm_model import HMMRegimeModel

MODEL_MAP = {
    "kmeans": KMeansRegimeModel,
    "gmm": GMMRegimeModel,
    "hmm": HMMRegimeModel,
}


def run_model(model_name, df=None, n_regimes=3):
    if df is None:
        df = load_feature_matrix()
    X = df.values.copy()

    model = MODEL_MAP[model_name](n_regimes=n_regimes)
    model.fit(X)

    df[f"regime_{model_name}"] = model.predict(X)
    print(df[f"regime_{model_name}"].value_counts(normalize=True))
    return df, model


def run_all_models(n_regimes=3):
    df = load_feature_matrix().sort_index().copy()

    X = df.values.copy()

    for model_name, model_cls in MODEL_MAP.items():
        model = model_cls(n_regimes=n_regimes)
        model.fit(X)
        probs = model.predict_proba(X) if model_name == "gmm" or model_name == "hmm" else None

        df[f"regime_{model_name}"] = model.predict(X)

        if probs is not None:
            for i in range(n_regimes):
                df[f"{model_name}_prob_{i}"] = probs[:, i]

    #print(df["regime_kmeans"].value_counts(normalize=True))
    #print(df["regime_gmm"].value_counts(normalize=True))
    #print(df["regime_hmm"].value_counts(normalize=True))


    return df


data = run_all_models(n_regimes=3)
run_model("kmeans")
run_model("gmm")
run_model("hmm")