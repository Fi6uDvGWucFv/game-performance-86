import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-86')

def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on exception."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay * (2 ** (attempt - 1)))
            
            logger.error(f"Final attempt failed after {max_attempts} retries")
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=0.5)
def fetch_game_data(url: str):
    """Mock network call for game performance metrics."""
    # Simulating actual network call
    return {"status": "ok", "url": url}