import logging
import sys
from typing import Optional

def setup_performance_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Initialize a configured logger for game performance metrics.

    Args:
        name: The name of the logger instance.
        level: The logging severity threshold.

    Returns:
        Configured logging.Logger instance.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(name)s: %(message)s'
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_performance_metric(logger: logging.Logger, metric: str, value: float) -> None:
    """
    Log specific performance metrics for the game engine.

    Args:
        logger: The logger instance to use.
        metric: The name of the performance metric.
        value: The measured value.
    """
    logger.info(f"PERF_METRIC: {metric} = {value}")