import os
from functools import lru_cache

class PerformanceConfig:
    """Configuration management with caching for game performance"""
    def __init__(self):
        self._settings = {
            "target_fps": int(os.getenv("TARGET_FPS", 144)),
            "render_scale": float(os.getenv("RENDER_SCALE", 1.0)),
            "max_draw_calls": int(os.getenv("MAX_DRAW_CALLS", 2000)),
            "enable_vsync": os.getenv("ENABLE_VSYNC", "true").lower() == "true"
        }

    @lru_cache(maxsize=16)
    def get_setting(self, key: str):
        """Cached retrieval of performance settings"""
        return self._settings.get(key)

    def update_setting(self, key: str, value):
        """Updates config and invalidates cache"""
        self._settings[key] = value
        self.get_setting.cache_clear()

# Global config instance
config = PerformanceConfig()