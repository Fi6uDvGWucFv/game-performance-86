import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', log_level=logging.INFO):
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(log_level)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    handler.setLevel(log_level)
    
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready.')