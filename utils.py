import json
from typing import Any, Dict, List


def load_game_data(file_path: str) -> Dict[str, Any]:
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} contains invalid JSON.")


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """Save game data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_game_scores(scores: List[Dict[str, Any]], min_score: int) -> List[Dict[str, Any]]:
    """Filter game scores above a minimum threshold."""
    return [score for score in scores if score.get('score', 0) >= min_score]
