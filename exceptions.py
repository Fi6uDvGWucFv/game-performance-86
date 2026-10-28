class PerformanceError(Exception):
    """Base exception for performance-related issues."""
    pass

class ResourceThrottleError(PerformanceError):
    """Raised when system resources reach capacity."""
    def __init__(self, resource_name, limit):
        self.message = f"Resource '{resource_name}' exceeded limit of {limit}"
        super().__init__(self.message)

class ProcessingLatencyError(PerformanceError):
    """Raised when operation exceeds time threshold."""
    def __init__(self, task_name, duration, threshold):
        self.message = f"Task '{task_name}' took {duration:.2f}s, exceeding {threshold}s limit"
        super().__init__(self.message)

class CacheOverflowError(PerformanceError):
    """Raised when memory cache hits storage ceiling."""
    def __init__(self, cache_size):
        self.message = f"Cache limit of {cache_size} bytes reached"
        super().__init__(self.message)

def check_performance_metric(metric, limit, name="metric"):
    """Validates performance constraints and raises errors."""
    if metric > limit:
        raise ProcessingLatencyError(name, metric, limit)
    return True