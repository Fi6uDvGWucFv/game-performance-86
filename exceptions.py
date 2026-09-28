import time
import functools
import logging

logger = logging.getLogger(__name__)

class NetworkError(Exception):
    """Custom exception for network-related failures."""
    pass

def retry_operation(retries=3, delay=1.0, backoff=2):
    """
    Decorator for retrying network operations with exponential backoff.
    
    :param retries: Number of attempts before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier for the delay after each failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, NetworkError) as e:
                    if i == retries - 1:
                        logger.error(f"Final attempt {i+1} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {i+1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator