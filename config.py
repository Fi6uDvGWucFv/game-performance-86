import json
import os

def load_config(file_path='config.json', defaults=None):
    # Load configuration from JSON file, using defaults if file is not found
    if defaults is None:
        defaults = {}
    
    if not os.path.exists(file_path):
        return defaults
    
    with open(file_path, 'r') as config_file:
        try:
            config = json.load(config_file)
        except json.JSONDecodeError:
            print('Error decoding JSON; using defaults.')
            return defaults
    
    # Update defaults with loaded config
    updated_config = {**defaults, **config}
    return updated_config

# Example usage
if __name__ == '__main__':
    default_config = {'volume': 100, 'resolution': '1920x1080'}
    config = load_config('settings.json', default_config)
    print(config)