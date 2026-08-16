import json
from typing import Any, Dict, List


def load_game_data(file_path: str) -> Dict[str, Any]:
    """
    Load game data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Dict[str, Any]: The loaded game data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """
    Save game data to a JSON file.
    
    Args:
        file_path (str): The path to save the JSON file.
        data (Dict[str, Any]): The game data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_high_scores(scores: List[Dict[str, Any]], min_score: int) -> List[Dict[str, Any]]:
    """
    Filter high scores above a minimum threshold.
    
    Args:
        scores (List[Dict[str, Any]]): List of player scores.
        min_score (int): The minimum score to filter.
    
    Returns:
        List[Dict[str, Any]]: Filtered list of scores.
    """
    return [score for score in scores if score['score'] > min_score]


def get_average_score(scores: List[Dict[str, Any]]) -> float:
    """
    Calculate the average score from a list.
    
    Args:
        scores (List[Dict[str, Any]]): List of player scores.
    
    Returns:
        float: The average score.
    """
    total_score = sum(score['score'] for score in scores)
    return total_score / len(scores) if scores else 0.0
