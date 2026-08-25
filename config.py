import json
from typing import Dict, Any, Optional

class GameConfig:
    """Manages game performance and display settings."""

    def __init__(self, config_path: str = "game_config.json") -> None:
        """Initialize GameConfig with optional config file path."""
        self.config_path: str = config_path
        self.settings: Dict[str, Any] = {
            "resolution": (1920, 1080),
            "target_fps": 60,
            "graphics_quality": "high",
            "fullscreen": True,
            "vsync_enabled": True,
            "anti_aliasing": "medium"
        }
        self._load_config()

    def _load_config(self) -> None:
        """Load settings from JSON file, falling back to defaults."""
        try:
            with open(self.config_path, "r") as file:
                loaded_settings: Dict[str, Any] = json.load(file)
                self.settings.update(loaded_settings)
        except (FileNotFoundError, json.JSONDecodeError):
            # Use default settings if file missing or invalid
            pass

    def get_setting(self, key: str) -> Optional[Any]:
        """Retrieve a configuration value by key."""
        return self.settings.get(key)

    def set_setting(self, key: str, value: Any) -> None:
        """Update a configuration value."""
        if key in self.settings:
            self.settings[key] = value

    def save(self) -> None:
        """Persist current settings to the config file."""
        with open(self.config_path, "w") as file:
            json.dump(self.settings, file, indent=2)

    def get_performance_settings(self) -> Dict[str, Any]:
        """Extract performance-related settings for optimization."""
        return {
            "target_fps": self.settings["target_fps"],
            "graphics_quality": self.settings["graphics_quality"],
            "vsync_enabled": self.settings["vsync_enabled"]
        }

    def update_resolution(self, width: int, height: int) -> None:
        """Set new resolution with type validation."""
        if width > 0 and height > 0:
            self.settings["resolution"] = (width, height)

def create_default_config(path: str) -> GameConfig:
    """Factory function to create and save default config."""
    config = GameConfig(path)
    config.save()
    return config

# Example usage for testing
if __name__ == "__main__":
    config = create_default_config("test_config.json")
    print(config.get_setting("target_fps"))
    config.set_setting("target_fps", 120)
    perf = config.get_performance_settings()
    print(perf)
    config.save()
