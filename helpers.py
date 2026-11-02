from typing import List, Dict, Union, Optional
import time

def calculate_frame_delta(timestamps: List[float]) -> float:
    """Calculates average time difference between consecutive frames in seconds."""
    if len(timestamps) < 2:
        return 0.0
    
    deltas = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    return sum(deltas) / len(deltas)

def format_performance_stats(metrics: Dict[str, Union[int, float]]) -> str:
    """Formats performance dictionary into a readable string for logging."""
    lines = [f"{key.upper()}: {value:.2f}" for key, value in metrics.items()]
    return " | ".join(lines)

def throttle_execution(interval_ms: int) -> None:
    """Pauses execution to maintain a target frame budget."""
    time.sleep(interval_ms / 1000.0)

def sanitize_input_values(data: Dict[str, Optional[float]]) -> Dict[str, float]:
    """Ensures all performance metrics are non-negative floats."""
    return {k: max(0.0, float(v or 0.0)) for k, v in data.items()}