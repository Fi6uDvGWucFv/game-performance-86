from typing import List, Dict, Union, Optional

class FrameProcessor:
    """Handles performance metrics calculation for game frames."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps: int = target_fps
        self.history: List[float] = []

    def calculate_average_latency(self, latencies: List[float]) -> float:
        """Compute the arithmetic mean of provided frame latencies."""
        if not latencies:
            return 0.0
        return sum(latencies) / len(latencies)

    def detect_stutter(self, frame_time: float, threshold_ms: float = 16.67) -> bool:
        """Check if a frame exceeds the target frame time budget."""
        return frame_time > threshold_ms

    def process_metrics(self, data: Dict[str, Union[int, float]]) -> Optional[Dict[str, float]]:
        """Aggregates raw performance metrics into a summary dictionary."""
        if not data:
            return None

        avg_latency: float = self.calculate_average_latency([float(data.get("latency", 0))])
        fps: float = 1000.0 / avg_latency if avg_latency > 0 else 0.0

        return {
            "avg_latency_ms": avg_latency,
            "calculated_fps": fps,
            "is_stable": fps >= self.target_fps
        }