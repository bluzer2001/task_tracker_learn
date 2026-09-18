import logging
from logging.handlers import RotatingFileHandler
from src.config.settings import LOGS_DIR, ROOT_LOG_FILENAME

LOG_CONFIG = {
    "log_file": LOGS_DIR / ROOT_LOG_FILENAME,
    "format": "%(asctime)s | %(name)s | %(processName)s | %(levelname)s | %(message)s",
}

def configure_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOG_CONFIG["format"])

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # file_handler = logging.FileHandler(LOG_CONFIG["log_file"], encoding="utf-8")
    # file_handler.setLevel(logging.INFO)
    # file_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_CONFIG["log_file"], maxBytes=1_000_000, backupCount=10, encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

