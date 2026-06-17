import json
from typing import Any, Dict, List


def load_game_data(file_path: str) -> Dict[str, Any]:
    """
    Loads game data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing game data.
    
    Returns:
        Dict[str, Any]: The parsed JSON data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """
    Saves game data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file where data will be saved.
        data (Dict[str, Any]): The game data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_players_by_score(players: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """
    Filters players based on their game score.
    
    Args:
        players (List[Dict[str, Any]]): A list of player data.
        threshold (float): The score threshold for filtering.
    
    Returns:
        List[Dict[str, Any]]: A list of players with scores above the threshold.
    """
    return [player for player in players if player.get('score', 0) > threshold]