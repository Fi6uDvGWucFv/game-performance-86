import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "game_performance", log_file: str = "logs/performance.log", level: int = logging.INFO) -> logging.Logger:
    """
    Sets up a rotating file logger and a console logger for game performance tracking.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent handler duplication if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Unified log format with timestamps
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for real-time stdout output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create directories for the log file if they do not exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Rotating file handler (rotates at 5MB, keeps last 3 logs)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Default active logger instance
logger = setup_logger()
