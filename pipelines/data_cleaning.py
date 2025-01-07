class DataCleaningPipeline:

    def clean_data_format(self) -> None:
        raise NotImplementedError

    def handle_missing_values(self) -> None:
        raise NotImplementedError

    def handle_outliers(self) -> None:
        raise NotImplementedError
