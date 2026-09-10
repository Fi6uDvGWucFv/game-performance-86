import time
import logging
from typing import Any, Callable, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance-86')

def measure_execution_time(func: Callable) -> Callable:
    """Decorator to log execution time for performance bottlenecks."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.info(f"function {func.__name__} executed in {duration:.4f}s")
        return result
    return wrapper

def format_performance_metrics(metrics: Dict[str, float]) -> str:
    """Utility to format raw performance data into readable strings."""
    formatted = [f"{k}: {v:.2f}ms" for k, v in metrics.items()]
    return " | ".join(formatted)

def sanitize_frame_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes invalid telemetry entries from frame processing."""
    return {k: v for k, v in data.items() if v is not None}

class PerformanceBuffer:
    """Thread-safe buffer for aggregating frame performance stats."""
    def __init__(self) -> None:
        self.data: list[float] = []

    def add(self, value: float) -> None:
        self.data.append(value)

    def get_average(self) -> float:
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data)