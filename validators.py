import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass

def validate_frame_rate(fps: int) -> bool:
    """Ensures frame rate remains within hardware bounds."""
    min_fps, max_fps = 30, 240
    try:
        if not isinstance(fps, int):
            raise TypeError(f"Expected integer for fps, got {type(fps).__name__}")
        if not (min_fps <= fps <= max_fps):
            raise ValueError(f"FPS {fps} outside allowed range ({min_fps}-{max_fps})")
        return True
    except (TypeError, ValueError) as e:
        logger.error(f"Frame rate validation failure: {e}")
        raise ValidationError(str(e)) from e

def sanitize_config_path(path: str) -> str:
    """Sanitizes and validates game configuration file paths."""
    if not path or not isinstance(path, str):
        logger.warning("Empty or invalid path provided, defaulting to system root")
        return "./config/default.json"
    
    # Prevent directory traversal attacks
    if ".." in path:
        logger.critical(f"Security violation attempt: {path}")
        raise ValidationError("Invalid path format detected")
    
    return path.strip()