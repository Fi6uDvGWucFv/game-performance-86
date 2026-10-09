from typing import List, Dict

def calculate_average_fps(frame_times_ms: List[float]) -> float:
    """Calculate the average frames per second from a list of frame times in milliseconds."""
    if not frame_times_ms:
        return 0.0
    total_time_s = sum(frame_times_ms) / 1000.0
    if total_time_s == 0:
        return 0.0
    return len(frame_times_ms) / total_time_s

def calculate_percentile_fps(frame_times_ms: List[float], percentile: float) -> float:
    """
    Calculate the FPS representation of a specific percentile of frame times.
    To find the 1% low (99th percentile of frame times): percentile = 99.0
    To find the 0.1% low (99.9th percentile of frame times): percentile = 99.9
    """
    if not frame_times_ms:
        return 0.0

    sorted_times = sorted(frame_times_ms)
    index = int(len(sorted_times) * (percentile / 100.0))
    index = min(max(index, 0), len(sorted_times) - 1)
    target_frame_time = sorted_times[index]

    if target_frame_time <= 0:
        return 0.0
    return 1000.0 / target_frame_time

def classify_performance_tier(avg_fps: float, low_1percent_fps: float) -> str:
    """Classify gaming performance tier based on average and 1% low FPS."""
    if avg_fps >= 120 and low_1percent_fps >= 90:
        return "competitive_excellent"
    elif avg_fps >= 60 and low_1percent_fps >= 45:
        return "smooth_high_quality"
    elif avg_fps >= 30 and low_1percent_fps >= 25:
        return "playable_console_like"
    elif avg_fps < 30:
        return "unplayable_stuttery"
    return "unstable_performance"

def get_performance_metrics(frame_times_ms: List[float]) -> Dict[str, float]:
    """Aggregate performance metrics from raw frame times."""
    if not frame_times_ms:
        return {"avg_fps": 0.0, "one_percent_low": 0.0, "zero_one_percent_low": 0.0}

    avg_fps = calculate_average_fps(frame_times_ms)
    one_percent_low = calculate_percentile_fps(frame_times_ms, 99.0)
    zero_one_percent_low = calculate_percentile_fps(frame_times_ms, 99.9)

    return {
        "avg_fps": round(avg_fps, 2),
        "one_percent_low": round(one_percent_low, 2),
        "zero_one_percent_low": round(zero_one_percent_low, 2)
    }