import time
from typing import Any, Callable, List

def throttle(interval: float):
    """Decorator to limit execution frequency of gaming logic."""
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def calculate_fps(frame_times: List[float]) -> float:
    """Calculate average frames per second from timing list."""
    if not frame_times:
        return 0.0
    return 1.0 / (sum(frame_times) / len(frame_times))

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Restrict game variable to specified bounds."""
    return max(min_val, min(value, max_val))

def format_latency(ms: float) -> str:
    """Format ping latency for ui display."""
    return f"{int(ms)}ms"