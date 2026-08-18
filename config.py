import json
import os

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found.')
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.data, file, indent=4)

# Usage example
# config = Config()
# print(config.get('screen_width', 800))
# config.set('screen_height', 600)