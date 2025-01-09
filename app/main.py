from app import logger
from stages import DataIngestion, DataCleaning

logger.info("Application started")

data_ingestion = DataIngestion()
data_cleaning = DataCleaning()

data_ingestion.run()
data_cleaning.run()
