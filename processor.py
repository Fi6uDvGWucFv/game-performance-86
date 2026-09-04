from typing import List, Dict, Optional

def normalize_frame_times(frame_times: List[float], target_fps: int = 60) -> List[float]:
    """Calculates frame time variance against target performance metrics."""
    if not frame_times:
        return []

    target_ms = 1000.0 / target_fps
    return [max(0.0, ft - target_ms) for ft in frame_times]

def calculate_hit_rate(hits: int, total_attempts: int) -> float:
    """Determines precision accuracy percentage for gaming events."""
    if total_attempts <= 0:
        return 0.0
    return (hits / total_attempts) * 100.0

def aggregate_telemetry(data: List[Dict[str, float]]) -> Dict[str, float]:
    """Computes average performance metrics from raw telemetry input."""
    if not data:
        return {"avg_fps": 0.0, "avg_latency": 0.0}

    keys = ["fps", "latency"]
    sums = {k: 0.0 for k in keys}
    for entry in data:
        for k in keys:
            sums[k] += entry.get(k, 0.0)

    count = len(data)
    return {f"avg_{k}": v / count for k, v in sums.items()}