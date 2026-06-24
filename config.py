import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 50,
    'language': 'en',
}

def load_config(filename='config.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                config = json.load(file)
            except json.JSONDecodeError:
                print('Error decoding JSON, using defaults.')
                return DEFAULT_CONFIG
            return {**DEFAULT_CONFIG, **config}
    else:
        print(f'Config file {filename} not found, using defaults.')
        return DEFAULT_CONFIG

config = load_config()  # Load configuration on module import