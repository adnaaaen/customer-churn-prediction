from src.stages import DataIngestion, DataCleaning, DataPreprocessing, ModelBuilding


def test_data_ingestion():
    data_ingestion = DataIngestion()
    assert data_ingestion.run() == True


def test_data_cleaning():
    data_cleaning = DataCleaning()
    assert data_cleaning.run() == True


def test_data_preprocessing():
    data_preprocessing = DataPreprocessing()
    assert data_preprocessing.run() == True


def test_model_building():
    model_building = ModelBuilding()
    assert model_building.run() == True
