from typing import Dict, List


def calculate_fps_metrics(frame_times_ms: List[float]) -> Dict[str, float]:
    """Calculates average, 1% low, and 0.1% low FPS from raw frame times.

    Args:
        frame_times_ms: List of individual frame durations in milliseconds.

    Returns:
        A dictionary containing critical gaming performance metrics.
    """
    if not frame_times_ms:
        return {
            "avg_fps": 0.0,
            "low_1percent_fps": 0.0,
            "low_01percent_fps": 0.0,
            "total_frames": 0.0
        }

    total_frames = len(frame_times_ms)
    total_time_ms = sum(frame_times_ms)
    total_time_s = total_time_ms / 1000.0
    avg_fps = total_frames / total_time_s if total_time_s > 0 else 0.0

    # Sort frame times to analyze percentiles (slowest frames at the end)
    sorted_times = sorted(frame_times_ms)

    # Calculate 1% low FPS
    count_1percent = max(1, int(total_frames * 0.01))
    worst_1percent_times = sorted_times[-count_1percent:]
    avg_1percent_time = sum(worst_1percent_times) / len(worst_1percent_times)
    low_1percent_fps = 1000.0 / avg_1percent_time if avg_1percent_time > 0 else 0.0

    # Calculate 0.1% low FPS
    count_01percent = max(1, int(total_frames * 0.001))
    worst_01percent_times = sorted_times[-count_01percent:]
    avg_01percent_time = sum(worst_01percent_times) / len(worst_01percent_times)
    low_01percent_fps = 1000.0 / avg_01percent_time if avg_01percent_time > 0 else 0.0

    return {
        "avg_fps": round(avg_fps, 2),
        "low_1percent_fps": round(low_1percent_fps, 2),
        "low_01percent_fps": round(low_01percent_fps, 2),
        "total_frames": float(total_frames)
    }
