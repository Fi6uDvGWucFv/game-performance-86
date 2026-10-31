from dataclasses import dataclass
from typing import List, Optional
import statistics


@dataclass
class FrameMetrics:
    """Calculated metrics for a set of frame render times."""
    avg_fps: float
    one_percent_low: float
    tenth_percent_low: float
    frame_time_variance: float
    total_frames: int


class FrameDataProcessor:
    """Processes raw frame times in milliseconds to compute telemetry metrics."""

    def __init__(self, target_fps: float = 60.0) -> None:
        self.target_fps: float = target_fps
        self._target_frame_time: float = 1000.0 / target_fps

    def process_frame_times(self, frame_times_ms: List[float]) -> Optional[FrameMetrics]:
        """Calculates average FPS, 1% low, 0.1% low, and variance from frame durations."""
        if not frame_times_ms:
            return None

        sorted_times: List[float] = sorted(frame_times_ms, reverse=True)
        total_frames: int = len(frame_times_ms)

        total_duration_s: float = sum(frame_times_ms) / 1000.0
        avg_fps: float = total_frames / total_duration_s if total_duration_s > 0 else 0.0

        one_percent_count: int = max(1, int(total_frames * 0.01))
        tenth_percent_count: int = max(1, int(total_frames * 0.001))

        one_percent_low_ms: float = statistics.mean(sorted_times[:one_percent_count])
        tenth_percent_low_ms: float = statistics.mean(sorted_times[:tenth_percent_count])

        one_percent_low_fps: float = 1000.0 / one_percent_low_ms if one_percent_low_ms > 0 else 0.0
        tenth_percent_low_fps: float = 1000.0 / tenth_percent_low_ms if tenth_percent_low_ms > 0 else 0.0

        variance: float = statistics.variance(frame_times_ms) if total_frames > 1 else 0.0

        return FrameMetrics(
            avg_fps=round(avg_fps, 2),
            one_percent_low=round(one_percent_low_fps, 2),
            tenth_percent_low=round(tenth_percent_low_fps, 2),
            frame_time_variance=round(variance, 4),
            total_frames=total_frames,
        )

    def identify_stutters(self, frame_times_ms: List[float], threshold_factor: float = 1.5) -> List[float]:
        """Filters frame times that exceed target duration by the specified factor."""
        threshold: float = self._target_frame_time * threshold_factor
        return [ft for ft in frame_times_ms if ft >= threshold]
