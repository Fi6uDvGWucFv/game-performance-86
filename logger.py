import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', log_level=logging.INFO, max_bytes=5*1024*1024, backup_count=5):
    # Create a directory for logs if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(handler)
    return logger

# Example of usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up.')