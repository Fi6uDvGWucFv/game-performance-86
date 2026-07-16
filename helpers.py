def calculate_fps(frames, elapsed_time):
    """
    Calculate Frames Per Second (FPS).
    
    Args:
        frames (int): Number of frames rendered.
        elapsed_time (float): Elapsed time in seconds.
    
    Returns:
        float: Calculated FPS.
    """
    if elapsed_time <= 0:
        return 0.0
    return frames / elapsed_time


def normalize_vector(vector):
    """
    Normalize a 3D vector.
    
    Args:
        vector (tuple): A tuple (x, y, z).
    
    Returns:
        tuple: Normalized vector.
    """
    import math
    length = math.sqrt(sum(v ** 2 for v in vector))
    if length == 0:
        return (0.0, 0.0, 0.0)
    return tuple(v / length for v in vector)


def load_json_file(filepath):
    """
    Load a JSON file and return its content.
    
    Args:
        filepath (str): Path to the JSON file.
    
    Returns:
        dict: Content of the JSON file.
    """
    import json
    with open(filepath, 'r') as file:
        return json.load(file)


def save_json_file(filepath, data):
    """
    Save data to a JSON file.
    
    Args:
        filepath (str): Path to save the JSON file.
        data (dict): Data to save.
    """
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)