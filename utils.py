import json


def load_game_data(file_path):
    """
    Load game data from a JSON file.
    
    :param file_path: str - Path to the JSON file containing game data.
    :return: dict - Parsed JSON data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise Exception('Error decoding JSON from the file.')


def save_game_data(file_path, data):
    """
    Save game data to a JSON file.
    
    :param file_path: str - Path to the JSON file to save data.
    :param data: dict - Data to save as JSON.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise Exception(f'Error writing to file: {file_path}')


def update_game_score(game_data, player_id, new_score):
    """
    Update the score for a player in game data.
    
    :param game_data: dict - Current game data.
    :param player_id: str - Player identification string.
    :param new_score: int - New score to be set.
    """
    if player_id in game_data:
        game_data[player_id]['score'] = new_score
    else:
        raise Exception(f'Player ID not found: {player_id}')