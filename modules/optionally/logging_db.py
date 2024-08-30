import logging


def logging_db():
    file_handler = logging.FileHandler('W:\\!VIOLETTA!\\!fw!\\journal\\db_log.txt')
    # file_handler = logging.FileHandler('db_log.txt')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger