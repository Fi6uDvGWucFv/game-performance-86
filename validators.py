import re
from typing import Any, Optional

# regex patterns for game asset identification
ASSET_ID_PATTERN = re.compile(r'^[a-z0-9_-]{8,32}$')

def validate_asset_id(asset_id: Any) -> bool:
    """verify asset identifiers conform to performance standards."""
    if not isinstance(asset_id, str):
        return False
    return bool(ASSET_ID_PATTERN.match(asset_id))

def sanitize_performance_metric(value: float, min_val: float = 0.0, max_val: float = 144.0) -> float:
    """clamp metric values to valid frame rate ranges."""
    return max(min_val, min(float(value), max_val))

def validate_config_schema(data: dict) -> bool:
    """ensure essential game settings are present."""
    required_keys = {'fps_target', 'render_scale', 'vsync'}
    return all(key in data for key in required_keys)

def get_validated_input(value: Any, default: Any) -> Any:
    """return input if valid else default fallback."""
    if value is not None:
        return value
    return default