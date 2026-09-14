import logging
import os
from datetime import datetime


LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)


# Get current date and time
now = datetime.now()

run_date = now.strftime("%Y-%m-%d")
run_time = now.strftime("%H%M%S")

DATE_LOGS_DIR = os.path.join(LOGS_DIR, run_date)
os.makedirs(DATE_LOGS_DIR, exist_ok=True)


RUN_LOG_FILE = os.path.join(DATE_LOGS_DIR, f"run_{run_time}.log")


logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(RUN_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)



def get_logger(name: str)-> logging.Logger:
    return logging.getLogger(name)
