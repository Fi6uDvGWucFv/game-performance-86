import math
from typing import Dict, List, Any, Optional

class PerformanceProcessor:
    """Processes gaming telemetry data with strict input validation."""

    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self.valid_records: List[Dict[str, Any]] = []

    def validate_payload(self, payload: Any) -> Optional[str]:
        """Validates a single telemetry payload. Returns None if valid, or an error message."""
        if not isinstance(payload, dict):
            return "Payload must be a dictionary"

        required_keys = {"fps", "frame_time_ms", "gpu_utilization"}
        if not required_keys.issubset(payload.keys()):
            missing = required_keys - payload.keys()
            return f"Missing required keys: {missing}"

        fps = payload.get("fps")
        frame_time = payload.get("frame_time_ms")
        gpu_util = payload.get("gpu_utilization")

        if not isinstance(fps, (int, float)) or fps <= 0 or math.isnan(fps):
            return f"Invalid FPS value: {fps}"

        if not isinstance(frame_time, (int, float)) or frame_time <= 0 or math.isnan(frame_time):
            return f"Invalid frame time value: {frame_time}"

        if not isinstance(gpu_util, (int, float)) or not (0 <= gpu_util <= 100) or math.isnan(gpu_util):
            return f"Invalid GPU utilization: {gpu_util}"

        return None

    def process_telemetry_batch(self, batch: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Processes a batch of game telemetry after validating each entry."""
        self.valid_records.clear()
        invalid_count = 0

        for record in batch:
            error = self.validate_payload(record)
            if error:
                # Skip record and record the telemetry validation failure
                invalid_count += 1
                continue
            self.valid_records.append(record)

        if not self.valid_records:
            return {"status": "error", "processed": 0, "invalid": invalid_count, "avg_fps": 0.0}

        total_fps = sum(r["fps"] for r in self.valid_records)
        avg_fps = total_fps / len(self.valid_records)

        return {
            "status": "success",
            "processed": len(self.valid_records),
            "invalid": invalid_count,
            "avg_fps": round(avg_fps, 2)
        }