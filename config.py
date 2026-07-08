import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'language': 'en',
    'difficulty': 'normal'
}

def load_config(file_path):
    """Load configuration from a JSON file, falling back on defaults if not found."""
    if not os.path.isfile(file_path):
        return DEFAULT_CONFIG
    
    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
        except json.JSONDecodeError:
            return DEFAULT_CONFIG
    
    return {**DEFAULT_CONFIG, **user_config}

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)