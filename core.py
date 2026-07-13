import json
from typing import Any, Dict, List

class GameDataHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> List[Dict[str, Any]]:
        """Load game data from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            return []

    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Save game data to a JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def update_data(self, updated_data: List[Dict[str, Any]]) -> None:
        """Update game data by merging new data."""
        current_data = self.load_data()
        current_data.extend(updated_data)
        self.save_data(current_data)

    def clear_data(self) -> None:
        """Clear all game data from the JSON file."""
        self.save_data([])

# Example usage:
# handler = GameDataHandler('game_data.json')
# handler.save_data([{'level': 1, 'score': 100}])
# print(handler.load_data())
