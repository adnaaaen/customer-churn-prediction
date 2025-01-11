from typing import Any
import os
import pandas as pd
import joblib
from config import ProjectPaths
from src.app import logger


DATASOURCE_PATH = ProjectPaths.get_dir("DATASET_PATH")
MODEL_PATH = ProjectPaths.get_dir("MODEL_PATH")


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


def save_joblib(data: Any, dir_name: str, path: str) -> bool:
    PATH_NAME = ProjectPaths.get_dir(dir_name)
    destination = os.path.join(PATH_NAME, path)
    if not os.path.exists(destination):
        os.makedirs(os.path.dirname(destination), exist_ok=True)
    joblib.dump(data, destination)
    logger.info(f"model saved as joblib in {destination}")
    return True


def load_joblib(dir_name: str, path: str) -> Any:
    PATH_NAME = ProjectPaths.get_dir(dir_name)
    destination = os.path.join(PATH_NAME, path)
    if os.path.exists(destination):
        data = joblib.load(destination)
        logger.error(f"joblib file loaded from {destination}")
        return data


def is_exists(path: str, filename: str) -> bool:

    PATH_NAME = ProjectPaths.get_dir(path)
    PATH_TO_CHECK = os.path.join(PATH_NAME, filename)
    if os.path.exists(PATH_TO_CHECK):
        logger.error(f"{PATH_TO_CHECK} : is exists!")
        return True
    return False
