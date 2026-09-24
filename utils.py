import time
import functools
import logging

logger = logging.getLogger('game-performance-86')

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

# Example usage for network calls
@retry_network_operation(max_retries=3)
def fetch_game_data(endpoint: str):
    """Mock network call for performance metrics."""
    # Logic would go here
    pass