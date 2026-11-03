"""Validation utilities for game performance telemetry and metric data."""

from typing import Any, Dict, List


def validate_fps_data(fps_values: List[float], max_fps: float = 1000.0) -> bool:
    """Validate that FPS measurements fall within realistic physical limits."""
    if not fps_values:
        return False
    return all(isinstance(fps, (int, float)) and 0.0 <= fps <= max_fps for fps in fps_values)


def validate_frame_times(frame_times: List[float]) -> List[float]:
    """Filter out anomalous or corrupted frame time values (in milliseconds)."""
    valid_times = []
    for ft in frame_times:
        if isinstance(ft, (int, float)) and 0.1 <= ft <= 5000.0:
            valid_times.append(float(ft))
    return valid_times


def validate_performance_payload(payload: Dict[str, Any]) -> bool:
    """Check if incoming telemetry payload has valid required gaming metrics."""
    required_keys = {"session_id", "timestamp", "fps_data", "gpu_usage"}
    if not isinstance(payload, dict):
        return False
    if not required_keys.issubset(payload.keys()):
        return False

    if not isinstance(payload["fps_data"], list):
        return False

    gpu_usage = payload.get("gpu_usage")
    if not isinstance(gpu_usage, (int, float)) or not (0.0 <= gpu_usage <= 100.0):
        return False

    return True
