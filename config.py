import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "vsync": True,
    "resolution": [1920, 1080],
    "enable_debug": False
}

def load_config(filepath: str = "settings.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load config, using defaults: {e}")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "settings.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save configuration: {e}")