import time
import functools
import logging

logger = logging.getLogger('game-performance-86')

def retry_network_operation(max_attempts=3, delay=1.0, backoff=2):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=0.5)
def fetch_game_data(endpoint):
    """Simulated network call to fetch player performance stats."""
    # Actual networking logic goes here
    return {'status': 'success', 'data': {}}

if __name__ == '__main__':
    try:
        data = fetch_game_data('api.server.internal/stats')
        print(data)
    except Exception as e:
        print(f"Operation failed: {e}")