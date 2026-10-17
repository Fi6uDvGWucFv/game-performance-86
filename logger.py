import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'game_perf', log_file: str = 'app.log'):
    """
    Configures a rotating file logger for performance metrics.
    Limits file size to 5MB with 3 backup rotations.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate log files to prevent storage overflow in gaming environments
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Output to console for real-time debugging
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger