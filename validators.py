from typing import Dict, Any, Tuple, List, Optional

class ValidationError(ValueError):
    """Custom exception raised when telemetry data fails validation."""
    pass

def validate_game_metrics(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates the incoming game performance metrics payload.
    
    Args:
        data: A dictionary containing metrics like 'fps', 'frame_time_ms', and 'memory_mb'.
        
    Returns:
        A tuple of (is_valid, error_message).
    """
    required_fields = {"fps", "frame_time_ms", "memory_mb"}
    
    # Check for missing fields
    missing_fields = required_fields - data.keys()
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Validate FPS (Frames Per Second)
    fps = data.get("fps")
    if not isinstance(fps, (int, float)):
        return False, "FPS must be a numeric value"
    if fps <= 0 or fps > 1000:
        return False, f"FPS value {fps} is out of realistic bounds (1-1000)"
    
    # Validate Frame Time in milliseconds
    frame_time = data.get("frame_time_ms")
    if not isinstance(frame_time, (int, float)):
        return False, "Frame time must be a numeric value"
    if frame_time <= 0 or frame_time > 1000:
        return False, f"Frame time {frame_time}ms is out of realistic bounds (0.1-1000)"
    
    # Validate Memory Usage in Megabytes
    memory = data.get("memory_mb")
    if not isinstance(memory, (int, float)):
        return False, "Memory usage must be a numeric value"
    if memory <= 0 or memory > 131072:  # Up to 128 GB
        return False, f"Memory usage {memory}MB is out of realistic bounds"
    
    return True, None

def filter_invalid_telemetry(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filters out invalid telemetry payloads in the primary processing loop.
    """
    validated_batch = []
    for record in batch:
        is_valid, _ = validate_game_metrics(record)
        if is_valid:
            validated_batch.append(record)
    return validated_batch
