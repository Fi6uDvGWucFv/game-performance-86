import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='game_performance', log_file='performance.log', level=logging.INFO):
    """Initializes a rotating file logger for performance monitoring."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # File rotation: 5MB max size, keep 3 historical backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional: Log to console as well
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Instantiate default performance logger
performance_logger = setup_logger()