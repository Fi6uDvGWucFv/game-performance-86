import logging
import os
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "game_performance.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB limit per log file
BACKUP_COUNT = 3


def setup_logger(
    name: str = "game_perf",
    log_dir: str = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    level: int = logging.INFO,
    max_bytes: int = MAX_LOG_SIZE,
    backup_count: int = BACKUP_COUNT,
) -> logging.Logger:
    """Configures a rotating logger for tracking FPS and system performance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding handlers multiple times if logger exists
    if logger.hasHandlers():
        return logger

    os.makedirs(log_dir, exist_ok=True)
    log_filepath = os.path.join(log_dir, log_file)

    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Setup file handler with size-based log rotation
    file_handler = RotatingFileHandler(
        filename=log_filepath,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Setup console handler for real-time output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Default logger instance for game performance monitoring
perf_logger = setup_logger()