import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, delay=2, backoff=2, exceptions=(Exception,)): 
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@with_retry(retries=3, delay=1)
def fetch_game_data(url):
    """Example usage for network data fetching."""
    # Simulating a network request
    return {"status": "success", "data": "game_metrics"}