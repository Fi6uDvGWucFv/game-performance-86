from typing import Dict, Any, Union

# Define acceptable ranges for game performance metrics
VALID_FPS_RANGE = (0, 300)
VALID_LATENCY_RANGE = (0, 1000)

def validate_input_data(data: Dict[str, Any]) -> bool:
    """Validates incoming game performance telemetry payload."""
    try:
        fps = data.get('fps')
        latency = data.get('latency')

        if not isinstance(fps, (int, float)) or not (VALID_FPS_RANGE[0] <= fps <= VALID_FPS_RANGE[1]):
            return False
            
        if not isinstance(latency, (int, float)) or not (VALID_LATENCY_RANGE[0] <= latency <= VALID_LATENCY_RANGE[1]):
            return False

        return True
    except (TypeError, AttributeError):
        return False

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures all input data follows strict schema requirements."""
    return {
        'fps': float(data.get('fps', 0)),
        'latency': float(data.get('latency', 0)),
        'timestamp': str(data.get('timestamp', 'unknown'))
    }