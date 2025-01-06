import logging
import os
import sys
from app.config import ProjectDirs

PROJECT_DIR = ProjectDirs.get_dir("PROJECT_DIR")
logging_fmt = (
    "%(asctime)s: %(levelname)s, on %(module)s, lineno=%(lineno)d, msg=%(message)s"
)
dir = os.path.join(PROJECT_DIR, "logs/")
os.makedirs(dir, exist_ok=True)
filename = os.path.join(dir, "application_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_fmt,
    handlers=[logging.FileHandler(filename), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("CreditCardFraud")
