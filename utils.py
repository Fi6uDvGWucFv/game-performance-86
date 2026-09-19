import math
from typing import List, Dict

def calculate_fps(frame_time_ms: float) -> float:
    """Convert frame time in milliseconds to frames per second."""
    if frame_time_ms <= 0:
        return 0.0
    return round(1000.0 / frame_time_ms, 2)

def calculate_percentiles(frame_times_ms: List[float]) -> Dict[str, float]:
    """
    Calculate performance metrics from raw frame times.
    Returns average FPS, 1% low FPS, and 0.1% low FPS.
    """
    if not frame_times_ms:
        return {"avg_fps": 0.0, "one_percent_low": 0.0, "zero_one_percent_low": 0.0}

    sorted_times = sorted(frame_times_ms)
    total_frames = len(sorted_times)
    
    # Calculate average FPS
    avg_frame_time = sum(sorted_times) / total_frames
    avg_fps = calculate_fps(avg_frame_time)

    # 1% low represents the 99th percentile of slow frame times
    one_percent_idx = max(1, math.floor(total_frames * 0.99)) - 1
    one_percent_low_fps = calculate_fps(sorted_times[one_percent_idx])

    # 0.1% low represents the 99.9th percentile of slow frame times
    zero_one_idx = max(1, math.floor(total_frames * 0.999)) - 1
    zero_one_percent_low_fps = calculate_fps(sorted_times[zero_one_idx])

    return {
        "avg_fps": avg_fps,
        "one_percent_low": one_percent_low_fps,
        "zero_one_percent_low": zero_one_percent_low_fps
    }

def format_memory_usage(bytes_val: int) -> str:
    """Convert memory usage in bytes to a human-readable gaming overlay format."""
    if bytes_val < 0:
        return "0.00 B"
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} TB"