import time
import functools
import logging
from typing import Callable, Any

# Configure logger for performance metrics
logger = logging.getLogger('game-performance-86')

def retry_network_op(retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
            
            logger.error(f"Final attempt failed for {func.__name__} after {retries} retries")
            raise last_exception
        return wrapper
    return decorator