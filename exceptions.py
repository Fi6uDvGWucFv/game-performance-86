class GamePerformanceError(Exception):
    """Base exception for the game-performance-86 package."""
    pass

class ResourceLoadError(GamePerformanceError):
    """Raised when a game asset fails to load."""
    pass

class FrameRateDropError(GamePerformanceError):
    """Raised when performance threshold is breached."""
    pass

class ConfigurationError(GamePerformanceError):
    """Raised when game settings are invalid."""
    pass

def raise_if_threshold_exceeded(fps: float, threshold: float = 30.0):
    """Validate performance metrics against system requirements."""
    if fps < threshold:
        raise FrameRateDropError(f"FPS {fps} is below minimum {threshold}")

def validate_resource_path(path: str):
    """Ensure paths exist to prevent runtime asset errors."""
    import os
    if not os.path.exists(path):
        raise ResourceLoadError(f"Asset path not found: {path}")

# Standardized error management for engine hooks
def handle_critical_failure(error: Exception):
    """Global catch point for engine-level crashes."""
    print(f"[CRITICAL] {type(error).__name__}: {error}")
    # Additional logic for logging to file or telemetry server
    raise error