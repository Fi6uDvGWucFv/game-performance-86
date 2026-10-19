import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='game_performance', log_file='game_perf.log', level=logging.INFO):
    """
    Configures a rotating file logger for performance tracking.
    Max file size: 5MB, keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
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
        
        # Add console output as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Global logger instance for game-performance-86
perf_logger = setup_logger()