import kagglehub
import shutil
import os


def get_from_kaggle(destination: str, kaggle_url: str) -> bool:
    if not os.listdir(destination):
        base_path = kagglehub.dataset_download(kaggle_url)
        for item in os.listdir(base_path):
            content = os.path.join(base_path, item)
            shutil.move(content, destination)
        os.rmdir(base_path)
        return True
    return False
