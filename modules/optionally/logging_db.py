import logging
from configuration.config import settings as conf

def logging_db():
    file_handler = logging.FileHandler(conf.logger_path)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger