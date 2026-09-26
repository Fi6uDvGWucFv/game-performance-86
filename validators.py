from typing import Any, Dict, List, Union

class ValidationError(Exception):
    """Custom exception raised when gaming performance data validation fails."""
    pass

def validate_fps_data(fps_readings: List[Union[int, float]]) -> bool:
    """
    Validates a list of FPS (frames per second) performance readings.
    Ensures readings are non-negative, realistic, and contain data.
    """
    if not fps_readings:
        raise ValidationError("FPS readings list cannot be empty.")
    
    for fps in fps_readings:
        if not isinstance(fps, (int, float)):
            raise ValidationError(f"Invalid FPS reading type: {type(fps).__name__}. Expected int or float.")
        if fps < 0:
            raise ValidationError(f"FPS cannot be negative: {fps}")
        if fps > 1000:  # Realistic upper limit for gaming hardware
            raise ValidationError(f"Unrealistic FPS reading detected: {fps}")
    return True

def validate_telemetry_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates gaming session telemetry report payloads.
    Expects: 'game_id' (str), 'average_fps' (float), and 'frame_times' (list of floats).
    """
    required_keys = {"game_id", "average_fps", "frame_times"}
    missing_keys = required_keys - payload.keys()
    if missing_keys:
        raise ValidationError(f"Missing required telemetry keys: {', '.join(missing_keys)}")

    if not isinstance(payload["game_id"], str) or not payload["game_id"].strip():
        raise ValidationError("game_id must be a non-empty string.")

    try:
        validate_fps_data([payload["average_fps"]])
    except ValidationError as e:
        raise ValidationError(f"Invalid average_fps: {e}")

    frame_times = payload["frame_times"]
    if not isinstance(frame_times, list):
        raise ValidationError("frame_times must be a list of float values.")

    for ft in frame_times:
        if not isinstance(ft, (int, float)) or ft <= 0:
            raise ValidationError(f"Invalid frame time: {ft}. Must be a positive millisecond measurement.")

    return payload
