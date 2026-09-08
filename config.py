"""Configuration management module for game performance tracking."""

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict


@dataclass
class PerformanceConfig:
    """Settings governing game performance profiling and optimization."""

    target_fps: int = 60
    max_memory_mb: int = 4096
    enable_dynamic_resolution: bool = True
    gpu_profiling_level: str = "medium"
    custom_metrics: Dict[str, bool] = field(
        default_factory=lambda: {"draw_calls": True, "frame_time": True}
    )


class ConfigManager:
    """Manages loading, updating, and saving gaming performance configuration files."""

    def __init__(self, config_path: str = "performance_config.json") -> None:
        """Initialize ConfigManager with path to settings file."""
        self.config_path: Path = Path(config_path)
        self.config: PerformanceConfig = PerformanceConfig()

    def load_config(self) -> PerformanceConfig:
        """Load performance settings from disk or return defaults if file missing."""
        if not self.config_path.exists():
            self.save_config()
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data: Dict[str, Any] = json.load(f)
                self.config = PerformanceConfig(**data)
        except (json.JSONDecodeError, TypeError):
            self.config = PerformanceConfig()

        return self.config

    def save_config(self) -> None:
        """Persist current performance settings to JSON file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(asdict(self.config), f, indent=4)

    def update_setting(self, key: str, value: Any) -> bool:
        """Update a specific configuration attribute if valid."""
        if hasattr(self.config, key):
            setattr(self.config, key, value)
            self.save_config()
            return True
        return False
