import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, backoff=1.5, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = backoff
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt {attempt} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

@with_retry(retries=3)
def fetch_game_data(endpoint):
    """
    Example network call wrapper for game server data.
    """
    # Simulated network logic would go here
    pass