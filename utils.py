import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Retry {attempts}/{max_attempts} for {func.__name__} after {sleep_time}s")
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator