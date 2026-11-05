import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "resolution": [1920, 1080],
    "fullscreen": True,
    "target_fps": 60,
    "vsync": True
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Load configuration from JSON with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not parse {filepath}, using defaults.")
    
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persist current configuration settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving config to {filepath}: {e}")