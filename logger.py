import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    # Create a logger with the specified name
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    handler.setLevel(level)
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(handler)
    
    return logger

# Example usage:
if __name__ == '__main__':
    log = setup_logger('game_logger', 'game.log')
    log.info('Logger is set up and ready!')