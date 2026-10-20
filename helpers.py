from typing import List, Dict, Union, Optional
import time

def calculate_frame_delta(timestamps: List[float]) -> float:
    """Calculates the average time difference between frames in seconds."""
    if len(timestamps) < 2:
        return 0.0
    diffs = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    return sum(diffs) / len(diffs)

def format_performance_metrics(metrics: Dict[str, Union[int, float]]) -> str:
    """Converts raw performance metrics into a human-readable display string."""
    output = []
    for key, value in metrics.items():
        formatted_val = f"{value:.2f}" if isinstance(value, float) else str(value)
        output.append(f"{key.replace('_', ' ').title()}: {formatted_val}")
    return " | ".join(output)

def get_gpu_load_status(load_percentage: float) -> str:
    """Determines the operational health status based on GPU load."""
    if load_percentage < 30.0:
        return "IDLE"
    elif load_percentage < 85.0:
        return "OPTIMAL"
    return "THROTTLING"

def filter_stuttering_frames(latencies: List[float], threshold_ms: float = 16.67) -> List[float]:
    """Returns a list of frames that exceeded the target frame time budget."""
    return [t for t in latencies if t > threshold_ms]