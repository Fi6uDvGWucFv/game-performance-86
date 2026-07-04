import json
import os

DEFAULT_CONFIG = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fullscreen': False,
    'volume': 0.8,
    'language': 'en'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()  # Start with defaults
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)  # Override defaults with user settings

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)  # Output the loaded config
