from pipelines import DataIngestionPipeline


def test_data_ingestion():
    data_ingestion = DataIngestionPipeline()
    assert data_ingestion.run() == True
