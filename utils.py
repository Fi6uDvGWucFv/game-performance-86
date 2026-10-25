"""Performance metrics calculation utilities for gaming benchmark data."""

from typing import Dict, List


def calculate_fps_metrics(frame_times_ms: List[float]) -> Dict[str, float]:
    """Calculate average FPS, 1% low FPS, and 0.1% low FPS from frame times.

    Args:
        frame_times_ms: List of frame durations measured in milliseconds.

    Returns:
        Dictionary containing avg_fps, low_1percent, and low_0_1percent.
    """
    if not frame_times_ms:
        return {"avg_fps": 0.0, "low_1percent": 0.0, "low_0_1percent": 0.0}

    # Convert frame times (ms) to FPS
    fps_values = [1000.0 / ft for ft in frame_times_ms if ft > 0]
    if not fps_values:
        return {"avg_fps": 0.0, "low_1percent": 0.0, "low_0_1percent": 0.0}

    sorted_fps = sorted(fps_values)
    total_frames = len(sorted_fps)

    # Calculate lower percentiles for drop/stutter assessment
    one_percent_idx = max(1, int(total_frames * 0.01))
    point_one_percent_idx = max(1, int(total_frames * 0.001))

    avg_fps = sum(sorted_fps) / total_frames
    low_1percent = sum(sorted_fps[:one_percent_idx]) / one_percent_idx
    low_0_1percent = sum(sorted_fps[:point_one_percent_idx]) / point_one_percent_idx

    return {
        "avg_fps": round(avg_fps, 2),
        "low_1percent": round(low_1percent, 2),
        "low_0_1percent": round(low_0_1percent, 2),
    }


def clean_frame_data(
    frame_times_ms: List[float], max_threshold_ms: float = 1000.0
) -> List[float]:
    """Filter out invalid or extreme outlier frame durations.

    Args:
        frame_times_ms: Raw frame duration measurements.
        max_threshold_ms: Upper bound for valid frame time in milliseconds.

    Returns:
        Filtered list of frame durations.
    """
    return [ft for ft in frame_times_ms if 0.1 <= ft <= max_threshold_ms]
