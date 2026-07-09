import json
from typing import List, Dict, Any


def calculate_average_frames(data: List[Dict[str, Any]]) -> float:
    """
    Calculate the average frames per second (FPS) from gaming data.
    
    Args:
        data (List[Dict[str, Any]]): List of dictionaries containing frame data.
    
    Returns:
        float: Average FPS calculated from the data.
    """
    total_frames = sum(entry['frames'] for entry in data)
    total_time = sum(entry['time'] for entry in data)  # Time in seconds
    average_fps = total_frames / total_time if total_time > 0 else 0
    return average_fps


def filter_high_performance(data: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """
    Filter the gaming data to only include entries with an FPS above the specified threshold.
    
    Args:
        data (List[Dict[str, Any]]): List of dictionaries containing frame data.
        threshold (float): Minimum FPS threshold for filtering.
    
    Returns:
        List[Dict[str, Any]]: Filtered list of performance entries.
    """
    return [entry for entry in data if (entry['frames'] / entry['time']) > threshold]  # FPS calculation


def save_performance_data(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Save the gaming performance data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (List[Dict[str, Any]]): List of dictionaries to save.
    """
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Save with pretty printing
