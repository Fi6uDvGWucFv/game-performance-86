import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'game_performance.log') -> logging.Logger:
    """Configures a rotating file logger for performance tracking."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate files at 5MB, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional: Add stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for game-performance-86 tracking
performance_logger = get_logger('performance_monitor')