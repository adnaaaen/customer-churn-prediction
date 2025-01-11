import pandas as pd
from src.app import logger
from src.utils import download_from_drive, load_dataset, save_dataset, is_exists


class DataIngestion:

    def download_dataset(self) -> bool:
        df_1_url = "muhammadshahidazeem/customer-churn-dataset"
        df_2_url = "muhammadshahidazeem/customer-churn-dataset"
        try:
            download_from_drive(path="raw/customer-chrun-train.csv", url=df_1_url)
            download_from_drive(path="raw/customer-chrun-test.csv", url=df_2_url)
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def contact_datasets(self) -> bool:
        try:
            train_df = load_dataset("raw/customer-churn-training.csv")
            test_df = load_dataset("raw/customer-churn-testing.csv")
            df = pd.concat([train_df, test_df])
            save_dataset(df=df, path="cleaned/merged.csv")
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def run(self) -> bool:
        if all(
            (
                is_exists(
                    "DATASET_PATH", "raw/customer_churn_dataset-training-master.csv"
                ),
                is_exists(
                    "DATASET_PATH", "raw/customer_churn_dataset-testing-master.csv"
                ),
            )
        ):
            logger.info("raw data alrady exists!, SKIP DATA INGESTION!")
            return True

        download_status = self.download_dataset()
        load_status = self.contact_datasets()
        if download_status and load_status:
            logger.info("DATA INGESTION PIPELINE RUN SUCCESSFULLY!")
            return True
        else:
            logger.error("DATA INGESTION PIPELINE FAILED!")
            return False
