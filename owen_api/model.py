import pathlib
import pickle

model_artifacts_path = pathlib.Path("/app/model_artifacts")
xgboost_model_path = model_artifacts_path / "xgboost-classifier.pkl"
with open(xgboost_model_path, "rb") as input_handle:
    xgboost_model = pickle.load(input_handle)
