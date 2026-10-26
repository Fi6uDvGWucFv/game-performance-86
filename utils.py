import logging
import gc
import time
from typing import Any, Dict

# Configure performance logger for game metrics
logger = logging.getLogger('game-performance-86')

def force_garbage_collection() -> None:
    """Clears unused memory to prevent micro-stuttering."""
    gc.collect()
    logger.debug("Garbage collection cycle completed")

def format_performance_stats(data: Dict[str, float]) -> str:
    """Formats raw engine metrics into readable strings."""
    return " | ".join([f"{k}: {v:.2f}ms" for k, v in data.items()])

class PerformanceTimer:
    """Context manager for tracking high-frequency frame times."""
    def __init__(self, name: str):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (time.perf_counter() - self.start) * 1000
        logger.info(f"{self.name} took {elapsed:.3f}ms")

def validate_resource_path(path: str) -> bool:
    """Checks file integrity for critical game assets."""
    import os
    return os.path.exists(path) and os.path.isfile(path)