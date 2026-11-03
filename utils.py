from typing import List, Dict, Union, Optional

# Standardized types for performance metrics
MetricValue = Union[int, float]
PerformanceData = Dict[str, MetricValue]

def calculate_average_fps(frame_times: List[float]) -> float:
    """Calculates average frames per second from a list of frame timings."""
    if not frame_times:
        return 0.0
    return 1.0 / (sum(frame_times) / len(frame_times))

def format_memory_usage(bytes_count: int) -> str:
    """Converts byte values into human-readable megabyte strings."""
    mb_value = bytes_count / (1024 * 1024)
    return f"{mb_value:.2f} MB"

def filter_stuttering_frames(frame_times: List[float], threshold: float = 0.033) -> List[float]:
    """Identifies frames that exceed the target frame time threshold."""
    return [t for t in frame_times if t > threshold]

def aggregate_performance_metrics(data_points: List[PerformanceData]) -> PerformanceData:
    """Collates multiple performance datasets into a single average dictionary."""
    if not data_points:
        return {}
    
    keys = data_points[0].keys()
    result = {}
    for key in keys:
        values = [d[key] for d in data_points if key in d]
        result[key] = sum(values) / len(values) if values else 0.0
    return result