import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
PERFORMANCE_LOG_FILENAME = "game_performance.log"


def setup_logger(
    name: str = "game_perf",
    log_dir: str = "logs",
    log_level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
) -> logging.Logger:
    """Configures and returns a logger with rotating file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(DEFAULT_LOG_FORMAT)

    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)
    log_filepath = os.path.join(log_dir, PERFORMANCE_LOG_FILENAME)

    # Rotating file handler for performance metrics archiving
    file_handler = RotatingFileHandler(
        log_filepath,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler for real-time monitoring during gameplay sessions
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Performance logger initialized: %s", log_filepath)
    return logger


def log_frame_metrics(logger: logging.Logger, frame_id: int, fps: float, frame_time_ms: float) -> None:
    """Convenience helper to record frame render performance metrics."""
    logger.info("Frame %d | FPS: %.2f | FrameTime: %.2f ms", frame_id, fps, frame_time_ms)
