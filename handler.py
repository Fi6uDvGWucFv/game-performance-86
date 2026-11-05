from typing import List, Dict, Optional

class GamePerformanceHandler:
    """Handles performance metrics for game sessions."""

    def __init__(self, session_id: str, threshold: float = 60.0) -> None:
        self.session_id: str = session_id
        self.threshold: float = threshold
        self.metrics: List[float] = []

    def add_metric(self, fps: float) -> None:
        """Record a new frame rate measurement."""
        self.metrics.append(fps)

    def get_average_fps(self) -> float:
        """Calculate the average FPS for the session."""
        if not self.metrics:
            return 0.0
        return sum(self.metrics) / len(self.metrics)

    def check_stability(self) -> Dict[str, bool]:
        """Check if current performance meets target thresholds."""
        avg_fps: float = self.get_average_fps()
        return {
            "is_stable": avg_fps >= self.threshold,
            "needs_optimization": avg_fps < self.threshold
        }

    def export_report(self) -> Dict[str, Optional[str]]:
        """Export session summary to a structured format."""
        return {
            "session": self.session_id,
            "avg_fps": str(self.get_average_fps()),
            "status": "optimal" if self.check_stability()["is_stable"] else "degraded"
        }