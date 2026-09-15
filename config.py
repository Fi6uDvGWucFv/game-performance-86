import json
import os

DEFAULT_CONFIG = {
    "resolution": "1920x1080",
    "vsync": True,
    "target_fps": 144,
    "texture_quality": "high"
}

def load_config(filepath="settings.json"):
    """Loads user configuration or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config, filepath="settings.json"):
    """Persists configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")