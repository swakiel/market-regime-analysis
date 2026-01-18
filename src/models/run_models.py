from features.feature_matrix import load_feature_matrix
from models.kmeans_model import KMeansRegimeModel
from models.gmm_model import GMMRegimeModel

MODEL_MAP = {
    "kmeans": KMeansRegimeModel,
    "gmm": GMMRegimeModel,
}


def run_model(model_name, df=None, n_regimes=3):
    if df is None:
        df = load_feature_matrix()
    X = df.values.copy()

    model = MODEL_MAP[model_name](n_regimes=n_regimes)
    model.fit(X)

    df[f"regime_{model_name}"] = model.predict(X)
    return df, model


def run_all_models(n_regimes=3):
    df = load_feature_matrix()
    X = df.values.copy()

    for model_name, model_cls in MODEL_MAP.items():
        model = model_cls(n_regimes=n_regimes)
        model.fit(X)
        df[f"regime_{model_name}"] = model.predict(X)
        if model_name == "gmm":
            gmm_probs = model.predict_proba(X)
            for i in range(n_regimes):
                df[f"gmm_prob_{i}"] = gmm_probs[:, i]

    print(df[[f"gmm_prob_{i}" for i in range(n_regimes)]].head())
    print(df[[f"gmm_prob_{i}" for i in range(n_regimes)]].sum(axis=1).head())

    return df
