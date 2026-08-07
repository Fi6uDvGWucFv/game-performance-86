import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name='GameLogger', log_file='game.log', level=logging.INFO):
    """Sets up a logger with rotation capability."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():  
        logger.addHandler(handler)

    return logger


# Example usage:
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready!')
    log.warning('This is a warning message.')
    log.error('This is an error message.')
