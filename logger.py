import logging
from logging.handlers import RotatingFileHandler

# Logger setup function

def setup_logger(log_file='game.log', max_size=5*1024*1024, backup_count=3):
    """Set up a logger with rotation."""
    # Create a custom logger
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)

    # Create a handler that writes log entries to a file,
    # rotating the log when it reaches a certain size
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
