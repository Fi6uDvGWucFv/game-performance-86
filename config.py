import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json', user_config_path='user_config.json'):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_default_config()
        user_config = self.load_user_config()
        config.update(user_config)
        return config

    def load_default_config(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f'Default config file not found: {self.default_config_path}')
        with open(self.default_config_path, 'r') as f:
            return json.load(f)

    def load_user_config(self):
        if not os.path.exists(self.user_config_path):
            return {}
        with open(self.user_config_path, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

config_loader = ConfigLoader()  # Instantiate the config loader

if __name__ == '__main__':
    print(config_loader.config)  # Print final merged configuration