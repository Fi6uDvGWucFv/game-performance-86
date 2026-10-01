import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_frame_rate_calculate(total_frames: int, elapsed_time: float) -> float:
    """Calculates average frame rate with division by zero protection."""
    if elapsed_time <= 0:
        logger.warning('Invalid elapsed time encountered, returning 0.0 fps')
        return 0.0
    
    try:
        return float(total_frames / elapsed_time)
    except (TypeError, ValueError) as e:
        logger.error(f'Calculation error: {e}')
        return 0.0

def parse_config_value(value: Any, default: Any) -> Any:
    """Safely parses config inputs with type fallback."""
    if value is None:
        return default
    
    try:
        # Ensure we are working with expected types for game settings
        if isinstance(default, bool) and not isinstance(value, bool):
            return str(value).lower() in ('true', '1', 'yes')
        return type(default)(value)
    except (ValueError, TypeError) as e:
        logger.warning(f'Falling back to default due to parse error: {e}')
        return default

def get_resource_path(resource_id: Optional[str]) -> str:
    """Validates resource path strings for engine loading."""
    if not resource_id or not isinstance(resource_id, str):
        logger.error('Invalid resource identifier provided')
        return 'assets/default.png'
    
    # Sanitize path to prevent directory traversal
    safe_id = resource_id.replace('..', '').lstrip('/')
    return f'assets/{safe_id}'