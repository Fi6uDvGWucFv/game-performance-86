import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-86')

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network-bound operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=0.5)
def fetch_game_data(endpoint: str):
    """Example network call implementation."""
    # Placeholder for actual socket/requests logic
    pass