import json
from typing import Any, Dict

DEFAULTS = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D'
    }
}

class ConfigLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.config = DEFAULTS.copy()
        self.load_config()

    def load_config(self) -> None:
        try:
            with open(self.filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except FileNotFoundError:
            print(f"Config file not found, using defaults.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON, using defaults.")

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def save(self) -> None:
        with open(self.filepath, 'w') as file:
            json.dump(self.config, file, indent=4)
