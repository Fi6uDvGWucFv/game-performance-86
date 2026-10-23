"""Performance metric utilities for game frame rate and timing analysis."""

from typing import List, Dict, Union


def calculate_fps(frame_times_ms: List[float]) -> float:
    """Calculate average frames per second from frame duration samples in milliseconds.

    Args:
        frame_times_ms: List of frame durations measured in milliseconds.

    Returns:
        Average frames per second, or 0.0 if input is empty or invalid.
    """
    if not frame_times_ms:
        return 0.0

    valid_times = [t for t in frame_times_ms if t > 0]
    if not valid_times:
        return 0.0

    avg_frame_time_sec = (sum(valid_times) / len(valid_times)) / 1000.0
    return round(1.0 / avg_frame_time_sec, 2) if avg_frame_time_sec > 0 else 0.0


def calculate_frame_time_percentile(
    frame_times_ms: List[float], percentile: float = 99.0
) -> float:
    """Calculate specific percentile frame time (e.g. 99th percentile for 1% lows).

    Args:
        frame_times_ms: List of frame durations measured in milliseconds.
        percentile: Target percentile rank between 0.0 and 100.0.

    Returns:
        Frame time value at the specified percentile in milliseconds.
    """
    if not frame_times_ms:
        return 0.0

    sorted_times = sorted(frame_times_ms)
    index = int((percentile / 100.0) * len(sorted_times))
    index = min(max(index, 0), len(sorted_times) - 1)
    return round(sorted_times[index], 2)


def evaluate_performance_tier(avg_fps: float, p99_ms: float) -> str:
    """Determine performance quality tier based on average FPS and 99th percentile frame time.

    Args:
        avg_fps: Average frames per second.
        p99_ms: 99th percentile frame time in milliseconds.

    Returns:
        Performance quality grade string ('excellent', 'good', 'fair', 'poor').
    """
    if avg_fps >= 60.0 and p99_ms <= 20.0:
        return "excellent"
    elif avg_fps >= 45.0 and p99_ms <= 33.3:
        return "good"
    elif avg_fps >= 30.0 and p99_ms <= 50.0:
        return "fair"
    return "poor"
