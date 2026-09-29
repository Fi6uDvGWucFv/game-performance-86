import math
from typing import List, Dict, Union

def calculate_fps_percentiles(frame_times: List[float], percentiles: List[float] = [0.01, 0.1, 0.99]) -> Dict[float, float]:
    """Calculates frame time percentiles for performance monitoring."""
    if not frame_times:
        return {p: 0.0 for p in percentiles}

    sorted_times = sorted(frame_times)
    results = {}
    
    for p in percentiles:
        index = math.ceil(p * len(sorted_times)) - 1
        index = max(0, min(index, len(sorted_times) - 1))
        results[p] = sorted_times[index]
        
    return results

def normalize_telemetry_data(data: Dict[str, Union[int, float]], target_range: float = 1.0) -> Dict[str, float]:
    """Scales raw performance metrics to a normalized floating point range."""
    max_val = max(data.values()) if data else 1.0
    return {k: (v / max_val) * target_range for k, v in data.items()}

def validate_frame_budget(frame_time_ms: float, refresh_rate_hz: int = 60) -> bool:
    """Checks if frame time stays within display refresh budget."""
    budget_ms = 1000 / refresh_rate_hz
    return frame_time_ms <= budget_ms