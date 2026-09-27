import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "enable_telemetry": True,
    "sampling_interval_ms": 100,
    "log_level": "INFO",
    "process_priority": "HIGH"
}

class ConfigLoader:
    """Handles loading, saving, and merging configuration with system defaults."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            self._save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            
            # Merge defaults with user settings to handle missing keys gracefully
            merged = DEFAULT_CONFIG.copy()
            if isinstance(user_config, dict):
                merged.update(user_config)
            return merged
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults if file is corrupt or unreadable
            return DEFAULT_CONFIG.copy()

    def _save_config(self, data: Dict[str, Any]) -> None:
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError:
            # Silently fail if unable to write config, preserving runtime execution
            pass

    def get(self, key: str) -> Any:
        """Retrieve configuration value with safety fallback to defaults."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key: str, value: Any) -> None:
        """Update dynamic config setting and persist changes locally."""
        self.config[key] = value
        self._save_config(self.config)
