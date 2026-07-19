import json
from typing import List, Dict


def load_game_data(file_path: str) -> List[Dict]:
    """
    Load game data from a JSON file.
    
    :param file_path: Path to the JSON file containing game data.
    :return: List of game data dictionaries.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: List[Dict]) -> None:
    """
    Save game data to a JSON file.
    
    :param file_path: Path to the JSON file to save data.
    :param data: List of game data dictionaries to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_high_scores(data: List[Dict], min_score: int) -> List[Dict]:
    """
    Filter game data for high scores.
    
    :param data: List of game data dictionaries.
    :param min_score: Minimum score threshold for filtering.
    :return: Filtered list of dictionaries with high scores.
    """
    return [entry for entry in data if entry.get('score', 0) >= min_score]


def get_average_score(data: List[Dict]) -> float:
    """
    Calculate average score from game data.
    
    :param data: List of game data dictionaries.
    :return: Average score as a float.
    """
    total_score = sum(entry.get('score', 0) for entry in data)
    return total_score / len(data) if data else 0.0
