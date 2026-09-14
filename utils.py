import json
from typing import Dict, Any, List

def calculate_fps_average(frame_times: List[float]) -> float:
    """Calculates average frames per second from a list of frame timings."""
    if not frame_times:
        return 0.0
    return 1000.0 / (sum(frame_times) / len(frame_times))

def serialize_game_state(state: Dict[str, Any]) -> str:
    """Converts dictionary game states to minified JSON strings."""
    try:
        return json.dumps(state, separators=(',', ':'))
    except (TypeError, ValueError) as e:
        return f'{{"error": "serialization_failed", "details": "{str(e)}"}}'

def normalize_input(value: float, min_val: float, max_val: float) -> float:
    """Clamps input values within game coordinate bounds."""
    return max(min_val, min(value, max_val))

def format_performance_metric(metric_name: str, value: float) -> str:
    """Generates formatted string for performance logging dashboards."""
    return f"{metric_name.upper()}: {value:.2f}"