class InputValidationError(Exception):
    """Custom exception for game input processing errors."""
    pass

def validate_game_input(data: dict) -> bool:
    """
    Validates incoming game state payloads for performance metrics.
    Ensures required fields exist and constraints are met.
    """
    required_fields = ['player_id', 'action_type', 'timestamp', 'latency_ms']
    
    # Check for missing keys
    for field in required_fields:
        if field not in data:
            raise InputValidationError(f"Missing required field: {field}")

    # Validate data types and ranges
    if not isinstance(data['player_id'], int):
        raise InputValidationError("player_id must be an integer")
    
    if not isinstance(data['latency_ms'], (int, float)) or data['latency_ms'] < 0:
        raise InputValidationError("latency_ms must be a non-negative number")

    return True

def sanitize_input(data: dict) -> dict:
    """
    Sanitizes game input strings to prevent injection or errors.
    """
    if 'action_type' in data:
        data['action_type'] = str(data['action_type']).strip().lower()[:32]
    return data