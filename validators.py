"""Game performance telemetry input validator."""

from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Custom exception raised when telemetry validation fails."""
    pass


def validate_frame_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate raw frame performance payload from main processing loop."""
    required_fields = ["frame_id", "fps", "frame_time_ms"]
    
    for field in required_fields:
        if field not in payload:
            raise ValidationError(f"Missing required field: '{field}'")

    frame_id = payload["frame_id"]
    if not isinstance(frame_id, int) or frame_id < 0:
        raise ValidationError("Field 'frame_id' must be a non-negative integer")

    fps = payload["fps"]
    if not isinstance(fps, (int, float)) or fps <= 0 or fps > 1000:
        raise ValidationError("Field 'fps' must be a float or int between 0 and 1000")

    frame_time = payload["frame_time_ms"]
    if not isinstance(frame_time, (int, float)) or frame_time < 0:
        raise ValidationError("Field 'frame_time_ms' must be a non-negative number")

    if "gpu_usage" in payload:
        gpu = payload["gpu_usage"]
        if not isinstance(gpu, (int, float)) or not (0.0 <= gpu <= 100.0):
            raise ValidationError("Field 'gpu_usage' must be a percentage between 0 and 100")

    if "cpu_usage" in payload:
        cpu = payload["cpu_usage"]
        if not isinstance(cpu, (int, float)) or not (0.0 <= cpu <= 100.0):
            raise ValidationError("Field 'cpu_usage' must be a percentage between 0 and 100")

    return payload


def validate_batch_input(batch: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Validate a batch of frame payloads, returning valid items and error messages."""
    if not isinstance(batch, list):
        raise ValidationError("Batch input must be a list of telemetry payloads")

    valid_records = []
    errors = []

    for idx, item in enumerate(batch):
        try:
            validated = validate_frame_data(item)
            valid_records.append(validated)
        except ValidationError as err:
            errors.append(f"Record {idx}: {str(err)}")

    return valid_records, errors
