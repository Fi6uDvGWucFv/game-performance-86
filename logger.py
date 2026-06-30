import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(handler)
    
    return logger

# Example usage:
logger = setup_logger()
logger.debug('Logger initialized for game performance tracking.')