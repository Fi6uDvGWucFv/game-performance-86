import logging
from logging.handlers import RotatingFileHandler

# Logger configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_FILE = 'game_performance.log'
LOG_SIZE = 10 * 1024 * 1024  # 10 MB
LOG_BACKUP_COUNT = 5

# Set up the logger
def setup_logger():
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_SIZE, backupCount=LOG_BACKUP_COUNT)
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(handler)
    return logger

# Global logger instance
logger = setup_logger()

if __name__ == '__main__':
    logger.info('Logger is set up and ready.')