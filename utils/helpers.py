import os
import pandas as pd
from config import ProjectPaths
from app import logger

DATASOURCE_PATH = ProjectPaths.get_dir("DATASET_PATH")


def load_dataset(path: str) -> pd.DataFrame:
    destination = os.path.join(DATASOURCE_PATH, path)
    if os.path.exists(destination):
        logger.info(f"dataset load from {destination}")
        return pd.read_csv(destination)


def save_dataset(df: pd.DataFrame, path: str) -> bool:
    destination = os.path.join(DATASOURCE_PATH, path)
    if not os.path.exists(destination):
        os.makedirs(os.path.dirname(destination), exist_ok=True)
    df.to_csv(destination, index=False)
    logger.info(f"dataset saved on {destination}")
    return True
