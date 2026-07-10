import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'up': 'W',
        'down': 'S',
        'left': 'A',
        'right': 'D',
        'shoot': 'SPACE'
    }
}

def load_config(file_path):
    if not os.path.isfile(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
            return {**DEFAULT_CONFIG, **user_config}
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON in configuration file')

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)