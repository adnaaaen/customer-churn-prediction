from pathlib import Path
import os


class ProjectPaths:
    PROJECT_PATH: Path = Path(__file__).resolve().parents[1]
    DATASET_PATH: str = os.path.join(PROJECT_PATH, "data")
    MODEL_PATH: str = os.path.join(PROJECT_PATH, "model")

    @classmethod
    def get_dir(cls, name: str) -> Path:
        return getattr(cls, name.upper())
