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
    X = df.values

    model = MODEL_MAP[model_name](n_regimes=n_regimes)
    model.fit(X)

    df[f"regime_{model_name}"] = model.predict(X)
    return df, model


def run_all_models(n_regimes=3):
    df = load_feature_matrix()

    for model_name, model_cls in MODEL_MAP.items():
        model = model_cls(n_regimes=n_regimes)
        model.fit(df.values)
        df[f"regime_{model_name}"] = model.predict(df.values)

    return df
