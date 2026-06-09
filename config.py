import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 50,
    'controls': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D',
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get_config(self):
        return self.config

# Usage Example
if __name__ == '__main__':
    config_loader = ConfigLoader()
    current_config = config_loader.get_config()
    print(current_config)