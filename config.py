import json
import os

class ConfigLoader:
    DEFAULT_CONFIG = {
        'screen_width': 800,
        'screen_height': 600,
        'fullscreen': False,
        'fps': 60,
        'audio_volume': 0.5,
    }

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        # Load config from a JSON file or use defaults
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    return {**self.DEFAULT_CONFIG, **json.load(file)}
                except json.JSONDecodeError:
                    print('Error: Invalid JSON format in config file. Using defaults.')
                    return self.DEFAULT_CONFIG
        else:
            print('Config file not found. Using defaults.')
            return self.DEFAULT_CONFIG

    def get(self, key):
        # Get a config value by key
        return self.config.get(key, None)

    def set(self, key, value):
        # Set a config value by key
        self.config[key] = value

    def save(self):
        # Save current configuration to the file
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)  
