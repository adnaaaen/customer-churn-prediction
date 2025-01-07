class DataPreprocessingPipeline:

    def feature_engineering(self) -> None:
        raise NotImplementedError

    def label_encoding(self) -> None:
        raise NotImplementedError

    def normalizing(self) -> None:
        raise NotImplementedError
