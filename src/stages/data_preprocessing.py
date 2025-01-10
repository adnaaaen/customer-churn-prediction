import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from utils import save_dataset, load_dataset, is_exists
from app import logger


class DataPreprocessing:

    def transform(self) -> bool:
        try:

            df = load_dataset("cleaned/cleaned.csv")
            X = df.drop(["churn"], axis=1)
            Y = df["churn"]

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
            preprocessed = pipeline.fit_transform(X)
            transformed_df = pd.DataFrame(preprocessed, columns=X.columns)
            transformed_df["churn"] = Y

            save_dataset(df=transformed_df, path="cleaned/transformed.csv")
            return True
        except Exception as e:
            logger.error(f"exception occured on data transformation : {e}")
            return False

    def run(self) -> bool:
        if is_exists("DATASET_PATH", "cleaned/transformed.csv"):
            logger.info("transformed dataset already exists, SKIP DATA PREPROCESSING!")
            return True
        transformed_status = self.transform()
        if transformed_status:
            logger.info("DATA PREPROCESSING PIPELINE RUN SUCCESSFULLY!")
            return True
        else:
            logger.error("DATA PREPROCESSING PIPELINE FAILED!")
            return False
