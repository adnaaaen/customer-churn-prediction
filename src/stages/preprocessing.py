from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.utils import load_dataset, is_exists, save_joblib
from src.app import logger


class DataPreprocessing:

    def transform(self) -> bool:
        try:

            df = load_dataset("cleaned/cleaned.csv")
            X = df.drop(["churn"], axis=1)

            categorical_features = X.select_dtypes("object").columns
            numerical_features = X.select_dtypes("number").columns
            categorical_pipeline = Pipeline(
                steps=[("encoder", OrdinalEncoder()), ("scaler", StandardScaler())]
            )

            numerical_pipeline = Pipeline(steps=[("scaler", StandardScaler())])

            pipeline = ColumnTransformer(
                transformers=[
                    ("numerical", numerical_pipeline, numerical_features),
                    ("categorical", categorical_pipeline, categorical_features),
                ]
            )
            preprocessed = pipeline.fit(X)
            save_joblib(preprocessed, "PIPELINE_PATH", "preprocessor.joblib")

            return True
        except Exception as e:
            logger.error(f"exception occured on data transformation : {e}")
            return False

    def run(self) -> bool:
        if is_exists("PIPELINE_PATH", "preprocessor.joblib"):
            logger.info(
                "preprocessor pipeline has already exists, SKIP DATA PREPROCESSING!"
            )
            return True
        transformed_status = self.transform()
        if transformed_status:
            logger.info("DATA PREPROCESSING PIPELINE RUN SUCCESSFULLY!")
            return True
        else:
            logger.error("DATA PREPROCESSING PIPELINE FAILED!")
            return False
