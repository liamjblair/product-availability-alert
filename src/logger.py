import logging
import sys

def setup_logger():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set level to debug
    file_handler = logging.FileHandler("/user/local/airflow/logs/shopping_availability_alert.log")
    file_handler.setLevel(logging.DEBUG)

    # Create a stream handler and set level to error
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.ERROR)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Set formatter for handlers
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger = setup_logger()
