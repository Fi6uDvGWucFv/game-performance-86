import time
import functools
import logging

# Configure logging for performance tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance')

def measure_execution_time(func):
    """Decorator to log the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def clamp(value, min_val, max_val):
    """Restrict a value between min and max bounds."""
    return max(min_val, min(value, max_val))

def format_memory(bytes_size):
    """Convert bytes to human-readable megabytes."""
    return f"{bytes_size / (1024 * 1024):.2f} MB"

def throttle(interval):
    """Simple throttle for frequent game loop calls."""
    last_called = [0.0]
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator