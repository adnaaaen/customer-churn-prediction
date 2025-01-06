import kagglehub
import shutil
import os

destination = "./data/raw/"
if os.path.exists(os.path.join(destination, "credircard.csv")):
    base_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

    path = shutil.move(os.path.join(base_path, "creditcard.csv"), destination)
    print(f"dataset downloaded at {path}")
    os.rmdir(base_path)
else:
    print(f"file already exist at {os.path.join(destination, 'creditcard.csv')}")
