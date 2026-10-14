import time
import functools
from typing import Callable, Any

def format_frame_time(ms: float) -> str:
    """Converts milliseconds to a readable string with unit."""
    return f"{ms:.2f}ms"

def throttle(interval: float):
    """Decorator to limit function call frequency in ms."""
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.perf_counter()
            if now - last_called[0] >= (interval / 1000.0):
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Ensures value stays within inclusive range."""
    return max(min_val, min(value, max_val))

def calculate_fps(delta_time: float) -> float:
    """Calculates frames per second from frame delta."""
    if delta_time <= 0:
        return 0.0
    return 1.0 / delta_time

def get_resource_path(filename: str) -> str:
    """Constructs asset path for game resources."""
    return f"assets/data/{filename}"