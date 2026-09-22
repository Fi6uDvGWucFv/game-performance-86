import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "fps_limit": 144,
    "resolution": [1920, 1080],
    "vsync": True,
    "texture_quality": "high"
}

def load_config(file_path: str = "settings.json") -> Dict[str, Any]:
    """Load configuration from JSON or return defaults if missing."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading config: {e}. Using defaults.")
            
    return config

def save_config(config: Dict[str, Any], file_path: str = "settings.json") -> bool:
    """Persist current configuration to disk."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError as e:
        print(f"Failed to save config: {e}")
        return False