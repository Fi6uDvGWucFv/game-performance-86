import json
from typing import Any, Dict


def load_game_data(file_path: str) -> Dict[str, Any]:
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return {}


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error: An IOError occurred while writing to {file_path}: {e}")


def update_game_data(file_path: str, new_data: Dict[str, Any]) -> None:
    """Update specific fields in game data."""
    current_data = load_game_data(file_path)
    current_data.update(new_data)
    save_game_data(file_path, current_data)

