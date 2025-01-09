import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from utils import save_dataset, load_dataset
from app import logger

class DataPreprocessing:

    df = load_dataset("cleaned/cleaned.csv")
    X = df.drop(["churn"], axis=1)
    Y = df["churn"]

    categorical_features = df.select_dtypes("object").columns
    numerical_features = df.select_dtypes("number").columns

    def transform(self) -> bool:
        categorical_pipeline = Pipeline(
            steps=[("encoder", OrdinalEncoder()()), ("scaler", StandardScaler())]
        )

        numerical_pipeline = Pipeline(steps=[("scaler", StandardScaler())])

        self.pipeline = ColumnTransformer(
            transformers=[
                ("numerical", numerical_pipeline, self.numerical_features),
                ("categorical", categorical_pipeline, self.categorical_features),
            ]
        )
        preprocessed = self.pipeline.fit_transform(self.X)
        preprocessed_df = pd.DataFrame(preprocessed, columns=self.X.columns)
        transformed_df = pd.concat([preprocessed_df, self.Y])

        save_dataset(df=transformed_df, path="cleaned/transformed.csv")
        return True

    def run(self) -> bool:
        transformed_status = self.transform()
        if transformed_status:
            logger.info("DATA PREPROCESSING PIPELINE RUN SUCCESSFULLY!")
            return True
        else:
            logger.error("DATA PREPROCESSING PIPELINE FAILED!")
            return False

