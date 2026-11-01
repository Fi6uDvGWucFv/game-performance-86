class InputValidationError(Exception):
    """Custom exception for game input processing errors."""
    pass

def validate_game_input(data: dict) -> bool:
    """
    Validates player input structure and constraints.
    Ensures critical gameplay metrics are within safe bounds.
    """
    required_keys = {'player_id', 'action_type', 'value'}
    
    if not all(key in data for key in required_keys):
        raise InputValidationError("Missing mandatory input fields")
    
    if not isinstance(data['player_id'], int) or data['player_id'] < 0:
        raise InputValidationError("Invalid player_id format")

    if not isinstance(data['value'], (int, float)) or not (-1000 <= data['value'] <= 1000):
        raise InputValidationError("Input value out of operational range")

    return True

def process_safe_input(raw_data: dict):
    """
    Orchestrates validation before core game logic.
    """
    try:
        if validate_game_input(raw_data):
            return True
    except InputValidationError as e:
        print(f"Validation failure in game loop: {e}")
        return False
    return False