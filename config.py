import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "resolution": "1920x1080",
    "vsync": False,
    "shadow_quality": "medium",
    "texture_filtering": "anisotropic_4x",
    "enable_overlay": True,
    "telemetry_interval_ms": 500,
    "max_frame_time_ms": 16.6,
}


class ConfigLoader:
    """Loads and manages gaming performance settings with default fallbacks."""

    def __init__(self, config_path: str = "performance_config.json") -> None:
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load settings from JSON file, merging with default options."""
        if not os.path.exists(self.config_path):
            self.save()
            return self.settings

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)

            # Merge user settings into defaults
            for key, default_val in DEFAULT_CONFIG.items():
                self.settings[key] = user_config.get(key, default_val)

        except (json.JSONDecodeError, IOError):
            # Fallback to default configuration on read error
            self.settings = DEFAULT_CONFIG.copy()

        return self.settings

    def save(self) -> None:
        """Save current settings to the configuration file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieve a specific configuration parameter."""
        return self.settings.get(key, fallback)
