from typing import List, Dict, Union, Optional

def calculate_frame_delta(timestamps: List[float]) -> List[float]:
    """Calculates time differences between sequential frame timestamps."""
    if len(timestamps) < 2:
        return []
    return [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]

def format_performance_metrics(metrics: Dict[str, Union[int, float]]) -> str:
    """Formats raw engine metrics into a readable summary string."""
    parts = [f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}" for k, v in metrics.items()]
    return " | ".join(parts)

def filter_stutter_frames(deltas: List[float], threshold_ms: float = 33.3) -> List[float]:
    """Returns only frames exceeding the specified stutter threshold."""
    return [d for d in deltas if d > (threshold_ms / 1000.0)]

def get_average_fps(deltas: List[float]) -> Optional[float]:
    """Calculates average frames per second from delta times."""
    if not deltas:
        return None
    avg_delta = sum(deltas) / len(deltas)
    return 1.0 / avg_delta if avg_delta > 0 else 0.0