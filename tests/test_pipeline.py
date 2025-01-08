from pipelines import DataIngestionPipeline, DataCleaningPipeline


def test_data_ingestion():
    data_ingestion = DataIngestionPipeline()
    assert data_ingestion.run() == True


def test_data_cleaning():
    data_cleaning = DataCleaningPipeline()
    assert data_cleaning.run() == True
