import time
import functools
import logging

# Setup basic logging for performance metrics
logger = logging.getLogger('game-performance-86')

def time_execution(func):
    """Decorator to measure execution time of performance-critical functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(f'{func.__name__} executed in {end - start:.4f}s')
        return result
    return wrapper

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Constrain a value between min and max bounds."""
    return max(min_val, min(value, max_val))

def format_memory(bytes_val: int) -> str:
    """Convert bytes into human-readable megabytes."""
    mb = bytes_val / (1024 * 1024)
    return f"{mb:.2f} MB"

def get_frame_delta(last_time: float) -> float:
    """Calculate time passed since last frame for engine synchronization."""
    current = time.perf_counter()
    delta = current - last_time
    return delta