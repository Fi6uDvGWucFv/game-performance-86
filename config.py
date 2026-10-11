import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "vsync": True,
    "resolution": [1920, 1080],
    "fullscreen": False,
    "audio_volume": 0.8
}

class ConfigLoader:
    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    user_data = json.load(f)
                    self.config.update(user_data)
            except (json.JSONDecodeError, IOError):
                # fallback to defaults if file is corrupt or unreadable
                pass
        return self.config

    def save(self, new_config: Dict[str, Any]) -> None:
        self.config.update(new_config)
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f, indent=4)

# global accessor for convenience
loader = ConfigLoader()
config = loader.load()