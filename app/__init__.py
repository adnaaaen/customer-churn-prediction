import logging
import os
import sys
from config.paths import ProjectPaths

PROJECT_DIR = ProjectPaths.get_dir("PROJECT_PATH")
logging_fmt = (
    "%(asctime)s: %(levelname)s, on %(module)s, lineno=%(lineno)d, %(message)s"
)
dir = os.path.join(PROJECT_DIR, "logs/")
os.makedirs(dir, exist_ok=True)
filename = os.path.join(dir, "app_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_fmt,
    handlers=[
        logging.FileHandler(filename, mode="w"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("CreditCardFraud")
