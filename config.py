import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "target_fps": 60,
    "monitor_interval_seconds": 1.0,
    "enable_telemetry": True,
    "log_level": "INFO",
    "output_directory": "./perf_logs",
    "alert_threshold_low_fps": 45,
}

class ConfigLoader:
    """Loads and manages game performance configuration settings with sensible defaults."""

    def __init__(self, filepath: str = "perf_config.json") -> None:
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration from file, falling back to defaults if missing or invalid."""
        if not os.path.exists(self.filepath):
            self.save()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                if isinstance(loaded_data, dict):
                    for key, value in loaded_data.items():
                        if key in self.config:
                            # Basic type matching validation based on defaults
                            if isinstance(value, type(self.config[key])):
                                self.config[key] = value
        except (json.JSONDecodeError, OSError):
            self.config = DEFAULT_CONFIG.copy()

    def save(self) -> None:
        """Saves current configuration state back to the file."""
        try:
            directory = os.path.dirname(os.path.abspath(self.filepath))
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        """Retrieves a configuration value safely with fallback to hardcoded default."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))