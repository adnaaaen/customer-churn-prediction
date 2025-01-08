from camel_converter import to_snake
from app import logger
from utils import load_dataset, save_dataset


class DataCleaningPipeline:

    def clean_data_format(self) -> bool:
        self.df = load_dataset("merged/customer_churn.csv")
        logger.info(">>>DATA FORMAT CLEANING START<<<")
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
            logger.info(">>>DATA FORMAT CLEANING END<<<")
            return True

        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURRED: {e}<<<")
            return False

    def handle_missing_values(self) -> bool:
        try:
            logger.info(">>>MISSING VALUES HANDLING START<<<")

            self.df = self.df.loc[self.df.isna().mean(axis=1) * 100 < 1]

            logger.info(">>>MISSING VALUES HANDLING END<<<")

            save_dataset(df=self.df, path="cleaned/cleaned.csv")
            return True
        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURRED: {e}<<<")
            return False

    def run(self) -> bool:
        if all((self.clean_data_format(), self.handle_missing_values())):
            logger.info(">>>DATA CLEANING PIPELINE RUN SUCCESSFULLY!<<<")
            return True

        logger.info(">>>DATA CLEANING PIPELINE FAILED SOMEWHERE!<<<")
        return False
