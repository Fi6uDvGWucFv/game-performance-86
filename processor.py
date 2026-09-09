import logging
from typing import Dict, Any, List

logger = logging.getLogger("game_performance")

class PerformanceProcessor:
    """Processes game telemetry data and validates inputs for performance analysis."""
    
    def __init__(self, fps_threshold: float = 30.0):
        self.fps_threshold = fps_threshold

    def validate_metrics(self, data: Dict[str, Any]) -> bool:
        """Validates that the incoming telemetry packet has correct types and ranges."""
        if not isinstance(data, dict):
            logger.warning("Invalid data format: expected dictionary.")
            return False
            
        required_keys = {"frame_time_ms", "fps", "memory_mb"}
        if not required_keys.issubset(data.keys()):
            logger.warning(f"Missing required performance metrics: {required_keys - data.keys()}")
            return False

        try:
            if not (0.0 < float(data["frame_time_ms"]) < 1000.0):
                logger.warning(f"Out of bounds frame_time_ms: {data['frame_time_ms']}")
                return False
            if not (0.0 <= float(data["fps"]) <= 1000.0):
                logger.warning(f"Unrealistic FPS value: {data['fps']}")
                return False
            if not (10.0 <= float(data["memory_mb"]) <= 65536.0):
                logger.warning(f"Unrealistic memory usage: {data['memory_mb']} MB")
                return False
        except (TypeError, ValueError) as err:
            logger.error(f"Data type validation failed: {err}")
            return False

        return True

    def process_telemetry_stream(self, stream: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Processes a batch of game performance telemetry with strict input validation."""
        processed_count = 0
        dropped_count = 0
        total_fps = 0.0

        for record in stream:
            if not self.validate_metrics(record):
                dropped_count += 1
                continue

            total_fps += float(record["fps"])
            processed_count += 1

        avg_fps = total_fps / processed_count if processed_count > 0 else 0.0
        return {
            "processed_records": processed_count,
            "dropped_records": dropped_count,
            "average_fps": round(avg_fps, 2),
            "performance_warning": avg_fps < self.fps_threshold if processed_count > 0 else False
        }