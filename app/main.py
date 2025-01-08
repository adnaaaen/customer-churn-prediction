from app import logger
from pipelines import DataIngestionPipeline, DataCleaningPipeline

logger.info("Application started")

data_ingestion = DataIngestionPipeline()
data_cleaning = DataCleaningPipeline()

data_ingestion.run()
data_cleaning.run()
