import time
import functools
import logging

# Logger for network-related performance events
logger = logging.getLogger('game-performance-86')

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator to implement exponential backoff retry logic."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error("Max retries reached. Operation failed.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=0.5)
def fetch_game_data(endpoint: str):
    """Mock function demonstrating network request logic."""
    # Simulating a brittle network call
    logger.info(f"Requesting data from {endpoint}")
    return {"status": "success"}