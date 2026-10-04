import re
from typing import Any, Optional

# Configuration patterns for game entity validation
UUID_PATTERN = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$')

def validate_player_id(player_id: Any) -> bool:
    """Checks if provided id string matches UUID format."""
    if not isinstance(player_id, str):
        return False
    return bool(UUID_PATTERN.match(player_id.lower()))

def validate_performance_metrics(fps: int, latency: int) -> bool:
    """Ensures metric values fall within acceptable game parameters."""
    # Reject invalid frame rates and extreme latency
    if fps < 0 or fps > 500:
        return False
    if latency < 0 or latency > 2000:
        return False
    return True

def sanitize_input(data: Optional[str]) -> str:
    """Removes whitespace and truncates unsafe input strings."""
    if not data:
        return ""
    return data.strip()[:255]