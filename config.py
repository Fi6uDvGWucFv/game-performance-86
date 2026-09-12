import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "max_memory_mb": 4096,
    "enable_overlay": True,
    "metrics_interval_sec": 1.0,
    "gpu_vendor": "auto",
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads and manages game performance profiling settings with fallback defaults."""

    def __init__(self, config_path: str = "game_config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, overlaying defaults if keys are missing."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        self.settings.update(user_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to parse {self.config_path}: {err}. Using defaults.")

        return self.settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def save(self) -> None:
        """Save active configuration back to disk."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)
