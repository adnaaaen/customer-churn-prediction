import kagglehub
import shutil
import os
from config import ProjectPaths
from app import logger

DATASOURCE_PATH = ProjectPaths.get_dir("DATASET_PATH")


def get_from_kaggle(path: str, url: str) -> bool:
    destination = os.path.join(DATASOURCE_PATH, path)
    if not os.path.exists(destination):
        os.makedirs(os.path.join(DATASOURCE_PATH, path), exist_ok=True)
    if not (os.listdir(destination)):
        base_path = kagglehub.dataset_download(url)
        for item in os.listdir(base_path):
            content = os.path.join(base_path, item)
            print(f"content path : {content}")
            print(f"destination path : {destination}")
            shutil.move(content, destination)
        os.rmdir(base_path)
        logger.info(f"dataset downloaded at : {destination} ")
        return True
    elif any(os.listdir(destination)):
        logger.info("dataset already exist!")
        return True
    return False
