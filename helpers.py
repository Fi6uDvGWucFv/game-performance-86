import functools
import time
from typing import Callable, Any

# Cache for compute-intensive game state lookups
_state_cache = {}

def memoize_state(func: Callable) -> Callable:
    """Decorator to cache game state results for performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _state_cache:
            _state_cache[key] = func(*args, **kwargs)
        return _state_cache[key]
    return wrapper

def clear_cache() -> None:
    """Manual trigger to clear memory during scene transitions."""
    _state_cache.clear()

def optimized_batch_update(data: list[dict], threshold: int = 1000) -> list[dict]:
    """
    Batch processing to minimize memory overhead during
    large object state synchronization.
    """
    if len(data) > threshold:
        return [d for d in data if d.get('is_active', False)]
    return data

@memoize_state
def calculate_delta_time(last_frame: float) -> float:
    """High-resolution delta calculation with memoization."""
    return time.perf_counter() - last_frame