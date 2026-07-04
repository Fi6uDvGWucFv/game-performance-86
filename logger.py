import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', max_bytes=10485760, backup_count=5):
    """Set up a logger with rotation."""
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger initialized and ready!')