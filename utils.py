import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2.0)
def fetch_game_data(endpoint):
    """Simulates a network request with retry logic."""
    # Implementation would typically use requests or aiohttp
    print(f"Fetching data from {endpoint}...")
    return {"status": "success"}