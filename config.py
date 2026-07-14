import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path) or {}
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        """Loads JSON configuration from a file."""
        if not os.path.isfile(path):
            return None
        with open(path, 'r') as file:
            return json.load(file)

    def merge_configs(self, default, user):
        """Merges user configuration over default."""
        merged = default.copy()  # Start with default config
        merged.update(user)      # Override with user config
        return merged

    def get(self, key, fallback=None):
        """Get a configuration value or fallback if not present."""
        return self.final_config.get(key, fallback)

# Usage:
# loader = ConfigLoader('default_config.json', 'user_config.json')
# value = loader.get('some_key', 'default_value')