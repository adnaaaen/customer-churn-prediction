from pandas import DataFrame
from .helpers import load_joblib

def predict_with_pipeline(input_data: DataFrame):
    MODEL = load_joblib("MODEL_PATH", "random_forest_model.joblib")
    return MODEL.predict(input_data)

