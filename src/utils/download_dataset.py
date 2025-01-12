import gdown
import os
from config import ProjectPaths
from src.app import logger

DATASOURCE_PATH = ProjectPaths.get_dir("DATASET_PATH")


def download_from_drive(path: str, url: str) -> bool:
    destination = os.path.join(DATASOURCE_PATH, path)
    if not os.path.exists(destination):
        os.makedirs(os.path.dirname(os.path.join(DATASOURCE_PATH, path)), exist_ok=True)
        gdown.download(url, destination)
        logger.info(f"dataset downloaded at : {destination} ")
        return True
    logger.info(f"dataset already exists on : {destination} ")
    return True
