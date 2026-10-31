def validate_input_data(data):
    """Validates player performance metrics input."""
    if not isinstance(data, dict):
        return False
    
    required_fields = {"fps": float, "frame_time": float, "gpu_load": float}
    
    for field, expected_type in required_fields.items():
        val = data.get(field)
        if val is None or not isinstance(val, expected_type):
            return False
        
        # Performance bounds checking
        if field == "fps" and (val < 0 or val > 1000):
            return False
        if field == "gpu_load" and (val < 0 or val > 100):
            return False
            
    return True

def process_game_loop(queue):
    """Main loop implementation with integrated validation."""
    processed_data = []
    for entry in queue:
        if validate_input_data(entry):
            # Sanitize and normalize frame time
            entry['frame_time'] = round(entry['frame_time'], 4)
            processed_data.append(entry)
        else:
            # Skip malformed data packets
            continue
    return processed_data