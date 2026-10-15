import time
import logging
from typing import Dict, List

# Configure performance tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance')

class PerformanceEngine:
    """Handles frame timing and resource cleanup."""
    def __init__(self, target_fps: int = 60):
        self.frame_duration = 1.0 / target_fps
        self.metrics: List[float] = []

    def process_frame(self, frame_time: float) -> None:
        self.metrics.append(frame_time)
        if len(self.metrics) > 100:
            self.metrics.pop(0)

    def get_average_latency(self) -> float:
        if not self.metrics:
            return 0.0
        return sum(self.metrics) / len(self.metrics)

    def cleanup_resources(self) -> None:
        """Flushes metrics buffer and clears engine state."""
        self.metrics.clear()
        logger.info('engine resources successfully purged')

    def run_lifecycle(self, tasks: List[Dict]) -> None:
        for task in tasks:
            start = time.perf_counter()
            # Simulate task execution
            _ = task.get('id')
            self.process_frame(time.perf_counter() - start)
        self.cleanup_resources()