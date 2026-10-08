import math
from typing import List

def calculate_fps(frame_times_ms: List[float]) -> float:
    """
    Calculate average Frames Per Second (FPS) from a list of frame times in milliseconds.
    """
    if not frame_times_ms:
        return 0.0
    total_time_seconds = sum(frame_times_ms) / 1000.0
    if total_time_seconds <= 0:
        return 0.0
    return len(frame_times_ms) / total_time_seconds

def calculate_percentile_fps(frame_times_ms: List[float], percentile: float) -> float:
    """
    Calculate the FPS equivalent for a specific percentile of frame times.
    Useful for computing 1% lows (99th percentile) and 0.1% lows (99.9th percentile).
    """
    if not frame_times_ms:
        return 0.0

    sorted_times = sorted(frame_times_ms)
    index = math.ceil((percentile / 100.0) * len(sorted_times)) - 1
    index = max(0, min(index, len(sorted_times) - 1))
    
    target_frame_time_ms = sorted_times[index]
    if target_frame_time_ms <= 0:
        return 0.0
    return 1000.0 / target_frame_time_ms

def calculate_stutter_index(frame_times_ms: List[float]) -> float:
    """
    Calculate the stutter index as the average absolute difference between consecutive 
    frame times in milliseconds. Lower values represent smoother gameplay.
    """
    if len(frame_times_ms) < 2:
        return 0.0

    differences = [
        abs(frame_times_ms[i] - frame_times_ms[i - 1])
        for i in range(1, len(frame_times_ms))
    ]
    return sum(differences) / len(differences)