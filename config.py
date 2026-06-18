import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 80,
    'controls': {
        'move_forward': 'W',
        'move_backward': 'S',
        'turn_left': 'A',
        'turn_right': 'D'
    }
}

class ConfigLoader:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filename):
            return DEFAULT_CONFIG
        with open(self.filename, 'r') as file:
            try:
                config = json.load(file)
            except json.JSONDecodeError:
                return DEFAULT_CONFIG
        return {**DEFAULT_CONFIG, **config}

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)
