import json
from typing import Any, Dict, List


def load_game_data(file_path: str) -> Dict[str, Any]:
    """
    Loads game data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing game data.
    
    Returns:
        dict: A dictionary containing the loaded game data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """
    Saves game data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (dict): The game data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_high_scores(scores: List[Dict[str, Any]], threshold: int) -> List[Dict[str, Any]]:
    """
    Filters high scores above a certain threshold.
    
    Args:
        scores (list): A list of score dictionaries.
        threshold (int): The score threshold to filter.
    
    Returns:
        list: A list of scores that exceed the threshold.
    """
    return [score for score in scores if score['score'] > threshold]


def calculate_average_score(scores: List[Dict[str, Any]]) -> float:
    """
    Calculates the average score from a list of score dictionaries.
    
    Args:
        scores (list): A list of score dictionaries.
    
    Returns:
        float: The average score.
    """
    if not scores:
        return 0.0
    total = sum(score['score'] for score in scores)
    return total / len(scores)