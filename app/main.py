from app import logger
from pipelines import DataIngestionPipeline

logger.info("Application started")

data_ingestion = DataIngestionPipeline()

data_ingestion.run()
