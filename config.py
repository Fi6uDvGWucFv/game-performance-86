import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise ConfigError(f"Configuration file not found: {self.filepath}")
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ConfigError(f"Error parsing JSON from {self.filepath}: {e}")
        except Exception as e:
            raise ConfigError(f"Unexpected error loading config: {e}")

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def save(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except IOError as e:
            raise ConfigError(f"Error saving config to {self.filepath}: {e}")
