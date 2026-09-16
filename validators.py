from typing import Union, Dict, Any

def validate_frame_data(data: Dict[str, Any]) -> bool:
    """
    Validates game telemetry data packets for frame stability.

    Args:
        data: A dictionary containing frame performance metrics.

    Returns:
        True if metrics are within acceptable thresholds, False otherwise.
    """
    required_keys = {"fps", "frame_time", "gpu_usage"}
    if not required_keys.issubset(data.keys()):
        return False

    return data["fps"] > 0 and data["frame_time"] < 50.0

def validate_player_latency(latency: Union[int, float]) -> bool:
    """
    Checks if player ping is suitable for competitive gaming.

    Args:
        latency: Current network latency in milliseconds.

    Returns:
        True if latency is below the competitive threshold of 100ms.
    """
    return 0 <= latency < 100

def sanitize_input(value: str) -> str:
    """
    Strips potential malicious characters from player chat or input.

    Args:
        value: Raw input string from the game client.

    Returns:
        A sanitized string safe for logging or database storage.
    """
    return "".join(char for char in value if char.isalnum() or char == " ")