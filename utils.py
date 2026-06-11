import json

class GameDataException(Exception):
    pass


def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise GameDataException(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise GameDataException(f'Error decoding JSON from: {file_path}')


def save_game_data(data, file_path):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise GameDataException(f'Error saving data to {file_path}: {str(e)}')


def update_game_data(file_path, updates):
    """Update specific fields in the game data."""
    data = load_game_data(file_path)
    data.update(updates)
    save_game_data(data, file_path)