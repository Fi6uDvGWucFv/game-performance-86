from functools import lru_cache
import re

# compiled regex patterns for performance
_ENTITY_ID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

@lru_cache(maxsize=1024)
def validate_entity_id(entity_id: str) -> bool:
    """validates entity strings using cached regex results"""
    if not entity_id or len(entity_id) > 64:
        return False
    return bool(_ENTITY_ID_PATTERN.match(entity_id))

def batch_validate_ids(id_list: list[str]) -> list[bool]:
    """bulk processing of id validation for frames"""
    return [validate_entity_id(uid) for uid in id_list]

class PerformanceValidator:
    """validator class with precomputed internal constraints"""
    __slots__ = ('threshold',)

    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold

    def check_frame_budget(self, frame_time: float) -> bool:
        """checks if frame performance meets thresholds"""
        return frame_time <= self.threshold