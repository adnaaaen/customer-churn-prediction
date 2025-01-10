from app import logger
from src.stages import DataIngestion, DataCleaning, DataPreprocessing, ModelBuilding

logger.info("Application started")

data_ingestion = DataIngestion()
data_cleaning = DataCleaning()
data_preprocessing = DataPreprocessing()
model_building = ModelBuilding()

data_ingestion.run()
data_cleaning.run()
data_preprocessing.run()
model_building.run()
