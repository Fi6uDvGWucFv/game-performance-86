import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 144,
    "vsync": False,
    "texture_quality": "high",
    "audio_enabled": True
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.data = self._load_or_default()

    def _load_or_default(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return DEFAULT_CONFIG
        
        try:
            with open(self.config_path, 'r') as f:
                loaded = json.load(f)
                return {**DEFAULT_CONFIG, **loaded}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def save(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.data, f, indent=4)

if __name__ == "__main__":
    loader = ConfigLoader()
    print(f"Current FPS limit: {loader.get('fps_limit')}")