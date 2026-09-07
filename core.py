import time
import logging
import functools
from typing import Callable, Any

logger = logging.getLogger('game-performance-86')

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying unstable network calls."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_game_data(endpoint: str):
    """Example network operation requiring robustness."""
    # Simulation of network interaction
    if not endpoint:
        raise ConnectionError("Failed to connect to game server")
    return {"status": "success", "data": "performance_metrics"}