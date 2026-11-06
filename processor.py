import logging
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)


class PerformanceDataProcessor:
    """Processes frame timing and GPU telemetry with edge case handling."""

    def __init__(self, target_framerate: float = 60.0):
        self.target_framerate = max(1.0, float(target_framerate)) if target_framerate else 60.0

    def calculate_frame_stats(self, raw_frame_times_ms: List[Any]) -> Dict[str, float]:
        """Calculates average FPS and 1% lows from raw frame durations."""
        valid_times: List[float] = []

        for raw_val in raw_frame_times_ms:
            try:
                val = float(raw_val)
                if 0.1 <= val <= 5000.0:
                    valid_times.append(val)
                else:
                    logger.warning(f"Discarding frame time out of bounds: {raw_val}ms")
            except (ValueError, TypeError):
                logger.warning(f"Discarding non-numeric frame sample: {raw_val}")

        if not valid_times:
            logger.error("No valid frame times available for analysis")
            return {"avg_fps": 0.0, "one_percent_low_fps": 0.0, "stutter_ratio": 0.0}

        total_time_sec = sum(valid_times) / 1000.0
        if total_time_sec <= 0:
            return {"avg_fps": 0.0, "one_percent_low_fps": 0.0, "stutter_ratio": 0.0}

        avg_fps = len(valid_times) / total_time_sec
        sorted_times = sorted(valid_times)

        one_percent_idx = max(1, int(len(sorted_times) * 0.99)) - 1
        worst_frame_time_ms = sorted_times[one_percent_idx]
        one_percent_low_fps = 1000.0 / worst_frame_time_ms if worst_frame_time_ms > 0 else 0.0

        target_frame_time_ms = 1000.0 / self.target_framerate
        stutter_count = sum(1 for t in valid_times if t > (target_frame_time_ms * 1.5))
        stutter_ratio = stutter_count / len(valid_times)

        return {
            "avg_fps": round(avg_fps, 2),
            "one_percent_low_fps": round(one_percent_low_fps, 2),
            "stutter_ratio": round(stutter_ratio, 4)
        }

    def sanitize_telemetry(self, raw_telemetry: Dict[str, Any]) -> Dict[str, Optional[float]]:
        """Sanitizes thermal and usage telemetry values against sensor anomalies."""
        sanitized: Dict[str, Optional[float]] = {}
        bounds = {
            "gpu_temp_c": (0.0, 120.0),
            "gpu_usage_pct": (0.0, 100.0),
            "vram_used_mb": (0.0, 128000.0)
        }

        for key, (min_val, max_val) in bounds.items():
            val = raw_telemetry.get(key)
            if val is None:
                sanitized[key] = None
                continue
            try:
                float_val = float(val)
                if min_val <= float_val <= max_val:
                    sanitized[key] = float_val
                else:
                    logger.warning(f"Telemetry key '{key}' out of range: {float_val}")
                    sanitized[key] = None
            except (ValueError, TypeError):
                logger.warning(f"Invalid telemetry type for key '{key}': {val}")
                sanitized[key] = None

        return sanitized
