import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_cap": 60,
    "vsync": True,
    "render_scale": 1.0,
    "audio_enabled": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads game configuration with system defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to disk."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)