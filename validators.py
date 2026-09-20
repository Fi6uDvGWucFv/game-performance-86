from typing import Any, Dict, Optional

def validate_game_input(data: Any) -> Optional[Dict[str, Any]]:
    """Validates input frame metrics for performance tracking."""
    if not isinstance(data, dict):
        return None

    required_fields = ['fps', 'frame_time_ms', 'gpu_load']
    if not all(k in data for k in required_fields):
        return None

    try:
        # Ensure numeric values are within reasonable gaming performance bounds
        validated_data = {
            'fps': float(data['fps']),
            'frame_time_ms': float(data['frame_time_ms']),
            'gpu_load': float(data['gpu_load'])
        }

        if validated_data['fps'] < 0 or validated_data['gpu_load'] < 0:
            return None

        return validated_data
    except (ValueError, TypeError):
        return None

def sanitize_player_metrics(raw_data: Any) -> Dict[str, Any]:
    """Sanitizes and filters player input metrics for processing loop."""
    valid_data = validate_game_input(raw_data)
    if valid_data is None:
        return {'status': 'error', 'message': 'invalid metric schema'}

    return {'status': 'success', 'data': valid_data}