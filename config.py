import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "resolution_scale": 1.0,
    "enable_vsync": True,
    "shadow_quality": "medium",
    "texture_filtering": "anisotropic_4x",
    "max_dynamic_lights": 16,
    "physics_ticks_per_second": 50,
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads and manages gaming performance configuration settings with sensible defaults."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file and merges it with defaults."""
        if not os.path.exists(self.config_path):
            self.save()
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                for key, value in user_config.items():
                    if key in DEFAULT_CONFIG:
                        self.config[key] = value
        except (json.JSONDecodeError, IOError):
            # Fail silently to guarantee fallback configuration is used
            pass

        return self.config

    def save(self) -> None:
        """Saves current configuration back to disk."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except IOError:
            # Prevent disk write errors from breaking game lifecycle
            pass

    def get(self, key: str) -> Any:
        """Retrieves a configuration value, falling back to default if unavailable."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
