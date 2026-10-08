import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2):
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
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Retry {attempt + 1}/{retries} after {current_delay}s delay")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

# Example usage for network-dependent game services
@retry_network_op(retries=3, delay=1)
def fetch_leaderboard_data(endpoint):
    """Placeholder for actual network call logic."""
    # Simulating transient network failure
    import random
    if random.random() < 0.5:
        raise ConnectionError("Server unreachable")
    return {"status": "success", "data": []}