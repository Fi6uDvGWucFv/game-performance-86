import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of game performance configurations."""
    
    DEFAULT_CONFIG = {
        "frame_rate_limit": 60,
        "enable_vsync": True,
        "graphics_preset": "medium",
        "debug_mode": False
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from file and merges with hardcoded defaults."""
        config = self.DEFAULT_CONFIG.copy()
        
        if not os.path.exists(self.config_path):
            return config
            
        try:
            with open(self.config_path, "r") as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

    def save(self, config: Dict[str, Any]) -> None:
        """Persists configuration dictionary to local storage."""
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=4)

if __name__ == "__main__":
    loader = ConfigLoader()
    current_config = loader.load()
    print(f"Active Configuration: {current_config}")