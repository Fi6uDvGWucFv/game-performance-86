import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', max_bytes=5*1024*1024, backup_count=5):
    """
    Sets up a rotating logger.
    
    Args:
        log_file (str): Name of the log file.
        max_bytes (int): Max bytes before rotation occurs.
        backup_count (int): Number of backup files to keep.
    """
    logger = logging.getLogger('game_performance_logger')
    logger.setLevel(logging.DEBUG)

    # Create handlers
    if not logger.hasHandlers():
        # Create a rotating file handler
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        handler.setLevel(logging.DEBUG)

        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message.')
    log.info('Logger setup complete.')
