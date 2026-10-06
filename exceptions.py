class PerformanceOptimizationError(Exception):
    """Base exception for performance monitoring failures."""
    pass

class ResourceConstraintError(PerformanceOptimizationError):
    """Raised when system resources fall below thresholds."""
    pass

class CacheOverflowError(PerformanceOptimizationError):
    """Raised when the memory cache exceeds capacity."""
    pass

def raise_if_bottleneck(metrics: dict, threshold: float = 0.95):
    """Validates resource usage against performance thresholds."""
    if metrics.get('cpu_usage', 0) > threshold:
        raise ResourceConstraintError('CPU utilization exceeding capacity')
    if metrics.get('memory_usage', 0) > threshold:
        raise CacheOverflowError('Memory allocation limit reached')

if __name__ == '__main__':
    # Example usage for performance monitoring
    stats = {'cpu_usage': 0.98, 'memory_usage': 0.45}
    try:
        raise_if_bottleneck(stats)
    except PerformanceOptimizationError as e:
        print(f'Performance bottleneck detected: {e}')