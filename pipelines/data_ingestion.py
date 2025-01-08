import os
import pandas as pd
from app import logger
from config.paths import ProjectPaths
from scripts import get_from_kaggle


class DataIngestionPipeline:
    DATASET_PATH = ProjectPaths.get_dir("DATASET_PATH")

    def download_dataset(self) -> bool:
        logger.info(">>>DATASET DOWNLOAD START<<<")
        kaggle_url = "muhammadshahidazeem/customer-churn-dataset"
        try:
            os.makedirs(os.path.join(self.DATASET_PATH, "raw"), exist_ok=True)
            get_from_kaggle(
                destination=os.path.join(self.DATASET_PATH, "raw"),
                kaggle_url=kaggle_url,
            )
            logger.info(
                f">>>dataset downloaded at : {os.path.join(self.DATASET_PATH, 'raw')} <<<"
            )
            logger.info(">>>DATASET DOWNLOAD END<<<")
            return True
        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURED : {e}<<<")
            return False

    def load_dataset(self) -> bool:
        logger.info(">>>DATA LOADING START<<<")
        try:
            train_df = pd.read_csv(
                os.path.join(
                    self.DATASET_PATH, "raw/customer_churn_dataset-training-master.csv"
                )
            )
            test_df = pd.read_csv(
                os.path.join(
                    self.DATASET_PATH, "raw/customer_churn_dataset-testing-master.csv"
                )
            )
            df = pd.concat([train_df, test_df])
            os.makedirs(os.path.join(self.DATASET_PATH, "merged"), exist_ok=True)
            df.to_csv(
                os.path.join(self.DATASET_PATH, "merged/customer_churn.csv"),
                index=False,
            )
            logger.info("combined dataset saved successfully")
            logger.info(">>>DATA LOADING END<<<")
            return True
        except Exception as e:
            logger.error(f">>>EXCEPTION OCCURED : {e}<<<")
            return False

    def run(self) -> bool:
        download_status = self.download_dataset()
        load_status = self.load_dataset()
        if download_status and load_status:
            logger.info(">>>DATA INGESTION PIPELINE RUN SUCCESSFULLY!<<<")
            return True
        else:
            logger.error(">>>DATA INGESTION PIPELINE FAILED SOMEWHERE!<<<")
            return False
