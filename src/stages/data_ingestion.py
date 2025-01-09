import pandas as pd
from app import logger
from utils import get_from_kaggle, load_dataset, save_dataset


class DataIngestion:

    def download_dataset(self) -> bool:
        kaggle_url = "muhammadshahidazeem/customer-churn-dataset"
        try:
            get_from_kaggle(
                path="raw",
                url=kaggle_url,
            )
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def contact_datasets(self) -> bool:
        try:
            train_df = load_dataset("raw/customer_churn_dataset-training-master.csv")
            test_df = load_dataset("raw/customer_churn_dataset-testing-master.csv")
            df = pd.concat([train_df, test_df])
            save_dataset(df=df, path="cleaned/merged.csv")
            return True
        except Exception as e:
            logger.error(f"exception occurred : {e}")
            return False

    def run(self) -> bool:
        download_status = self.download_dataset()
        load_status = self.contact_datasets()
        if download_status and load_status:
            logger.info("DATA INGESTION PIPELINE RUN SUCCESSFULLY!")
            return True
        else:
            logger.error("DATA INGESTION PIPELINE FAILED!")
            return False
