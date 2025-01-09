from src.stages import DataIngestion, DataCleaning


def test_data_ingestion():
    data_ingestion = DataIngestion()
    assert data_ingestion.run() == True


def test_data_cleaning():
    data_cleaning = DataCleaning()
    assert data_cleaning.run() == True
