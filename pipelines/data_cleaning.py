import pandas as pd
import os
from camel_converter import to_snake
from config import ProjectPaths
from app import logger


class DataCleaningPipeline:
    DATASET_PATH = ProjectPaths.get_dir("DATASET_PATH")
    df = pd.read_csv(os.path.join(DATASET_PATH, "merged/customer_churn.csv"))

    def clean_data_format(self) -> bool:
        logger.info(">>>DATA FORMAT CLEARNING START<<<")
        try:

            # change column format into snake case
            self.df.columns = [
                to_snake(column).replace(" ", "") for column in self.df.columns
            ]

            # drop unwanted features
            self.df = self.df.drop(["customer_i_d"], axis=1)

            # change dtypes
            to_integer = self.df.drop(
                ["total_spend", "gender", "subscription_type", "contract_length"],
                axis=1,
            ).columns
            self.df[to_integer] = self.df[to_integer].astype(dtype="Int16")
            logger.info(">>>DATA FORMAT CLEARNING END<<<")
            return True

        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURED: {e}<<<")
            return False

    def handle_missing_values(self) -> bool:
        try:
            logger.info(">>>MISSING VALUES HANDLING START<<<")
            self.df = self.df.loc[self.df.isna().mean(axis=1) * 100 < 1]
            logger.info(">>>MISSING VALUES HANDLING END<<<")
            return True
        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURED: {e}<<<")
            return False

    def save_cleaned_df(self) -> bool:
        try:
            logger.info(">>>MISSING VALUES HANDLING START<<<")
            if not os.path.exists(os.path.join(self.DATASET_PATH, "cleaned")):
                os.makedirs(os.path.join(self.DATASET_PATH, "cleaned"), exist_ok=True)
                self.df.to_csv(os.path.join(self.DATASET_PATH, "cleaned/cleaned.csv"))
            logger.info(
                f">>>cleaned dataset saved in: {os.path.join(self.DATASET_PATH, 'cleaned')} <<<"
            )
            logger.info(">>>MISSING VALUES HANDLING END<<<")
            return True
        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURED: {e}<<<")
            return False

    def run(self) -> bool:
        if all(
            (
                self.clean_data_format(),
                self.handle_missing_values(),
                self.save_cleaned_df(),
            )
        ):
            logger.info(">>>DATA CLEANING PIPELINE RUN SUCCESSFULLY!<<<")
            return True

        logger.info(">>>DATA CLEANING PIPELINE FAILED SOMEWHERE!<<<")
        return False
