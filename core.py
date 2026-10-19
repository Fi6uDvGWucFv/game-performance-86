import time
from typing import List, Dict, Union

class FrameDataProcessor:
    """Handles temporal game telemetry for performance monitoring."""

    def __init__(self, buffer_size: int = 60):
        self.buffer_size = buffer_size
        self.frame_times: List[float] = []

    def add_frame(self, frame_time_ms: float) -> None:
        """Adds a new frame duration and maintains buffer size."""
        if len(self.frame_times) >= self.buffer_size:
            self.frame_times.pop(0)
        self.frame_times.append(frame_time_ms)

    def calculate_metrics(self) -> Dict[str, Union[float, int]]:
        """Computes current fps and frame variance."""
        if not self.frame_times:
            return {"fps": 0.0, "variance": 0.0}

        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        fps = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0.0
        
        # Simple variance calculation
        variance = sum((x - avg_frame_time) ** 2 for x in self.frame_times) / len(self.frame_times)
        
        return {
            "fps": round(fps, 2),
            "avg_ms": round(avg_frame_time, 2),
            "variance": round(variance, 2)
        }

def get_timestamp() -> float:
    """Returns high-resolution timestamp for frame delta calculation."""
    return time.perf_counter() * 1000