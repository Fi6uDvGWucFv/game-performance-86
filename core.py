from typing import List, Dict, Optional
import time

class FrameTracker:
    """Tracks frame rendering performance metrics."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps: int = target_fps
        self.frame_times: List[float] = []

    def record_frame(self, duration: float) -> None:
        """Stores a frame duration in milliseconds."""
        self.frame_times.append(duration)
        if len(self.frame_times) > 1000:
            self.frame_times.pop(0)

    def get_average_fps(self) -> float:
        """Calculates average FPS over tracked samples."""
        if not self.frame_times:
            return 0.0
        avg_ms: float = sum(self.frame_times) / len(self.frame_times)
        return 1000.0 / avg_ms if avg_ms > 0 else 0.0

class PerformanceOptimizer:
    """Handles dynamic adjustment of graphical settings."""

    def __init__(self, thresholds: Dict[str, float]) -> None:
        self.thresholds: Dict[str, float] = thresholds

    def check_stability(self, current_fps: float) -> str:
        """Determines if current performance meets targets."""
        if current_fps < self.thresholds.get("min_fps", 30.0):
            return "LOWER_QUALITY"
        elif current_fps > self.thresholds.get("max_fps", 120.0):
            return "RAISE_QUALITY"
        return "OPTIMAL"