import pandas as pd
from config import logger
from src.utils import download_from_drive, load_dataset, save_dataset, is_exists


class DataIngestion:

    def download_dataset(self) -> bool:
        df_1_url = "https://drive.google.com/uc?id=1yn17jpwzGSHd-D0UamL2iAVuycfkZvkR"
        df_2_url = "https://drive.google.com/uc?id=1JSLW6XOfxHHE912SbhRb2YtAdvWOGlBf"
        try:
            download_from_drive(path="raw/customer-churn-train.csv", url=df_1_url)
            download_from_drive(path="raw/customer-churn-test.csv", url=df_2_url)
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def contact_datasets(self) -> bool:
        try:
            train_df = load_dataset("raw/customer-churn-train.csv")
            test_df = load_dataset("raw/customer-churn-test.csv")
            df = pd.concat([train_df, test_df])
            save_dataset(df=df, path="cleaned/merged.csv")
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def run(self) -> bool:
        if all(
            (
                is_exists("DATASET_PATH", "raw/customer-churn-train.csv"),
                is_exists("DATASET_PATH", "raw/customer-churn-test.csv"),
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
