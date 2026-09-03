import statistics
from typing import List, Dict

def calculate_frame_metrics(frame_times_ms: List[float]) -> Dict[str, float]:
    """
    Calculate key performance metrics from a list of frame times in milliseconds.
    
    Args:
        frame_times_ms: List of frame rendering durations in milliseconds.
        
    Returns:
        Dictionary containing average FPS, 1% low FPS, and stutter count.
    """
    if not frame_times_ms:
        return {"avg_fps": 0.0, "one_percent_low_fps": 0.0, "stutter_count": 0}
    
    # Calculate average FPS
    avg_frame_time = statistics.mean(frame_times_ms)
    avg_fps = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0.0
    
    # Calculate 1% low FPS (99th percentile frame times)
    sorted_times = sorted(frame_times_ms)
    percentile_index = int(len(sorted_times) * 0.99)
    percentile_index = min(percentile_index, len(sorted_times) - 1)
    p99_frame_time = sorted_times[percentile_index]
    one_percent_low_fps = 1000.0 / p99_frame_time if p99_frame_time > 0 else 0.0
    
    # Identify stutters (frame time > 2.0x the average)
    stutter_threshold = avg_frame_time * 2.0
    stutter_count = sum(1 for ft in frame_times_ms if ft > stutter_threshold)
    
    return {
        "avg_fps": round(avg_fps, 2),
        "one_percent_low_fps": round(one_percent_low_fps, 2),
        "stutter_count": stutter_count
    }
