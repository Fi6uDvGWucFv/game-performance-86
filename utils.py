import json


def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return None


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: An IOError occurred while writing to {file_path}.")


def get_high_scores(data):
    """Extract high scores from game data."""
    if not isinstance(data, dict):
        return []
    return sorted(data.get('high_scores', []), reverse=True)


def update_high_scores(data, new_score):
    """Update high scores with a new score if it's high enough."""
    if 'high_scores' not in data:
        data['high_scores'] = []
    if len(data['high_scores']) < 10 or new_score > min(data['high_scores']):
        data['high_scores'].append(new_score)
        data['high_scores'] = sorted(data['high_scores'], reverse=True)[:10]
