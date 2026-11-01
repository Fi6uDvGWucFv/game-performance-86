import os
from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    target_fps: int = 144
    render_scale: float = 1.0
    enable_vsync: bool = False
    max_texture_memory: int = 4096

def load_performance_settings() -> GameConfig:
    """Parses environment overrides for game engine optimization."""
    return GameConfig(
        target_fps=int(os.getenv("GAME_FPS", 144)),
        render_scale=float(os.getenv("GAME_SCALE", 1.0)),
        enable_vsync=os.getenv("GAME_VSYNC", "false").lower() == "true",
        max_texture_memory=int(os.getenv("GAME_VRAM_LIMIT", 4096))
    )

# Global configuration instance
settings = load_performance_settings()