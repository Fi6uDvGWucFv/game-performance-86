class PerformanceError(Exception):
    """Base exception for all game performance errors."""
    pass

class TelemetryDataError(PerformanceError):
    """Raised when game telemetry data is malformed."""
    pass

class LatencyThresholdExceeded(PerformanceError):
    """Raised when network latency exceeds allowed limits."""
    def __init__(self, latency: float, limit: float):
        self.latency = latency
        self.limit = limit
        super().__init__(f"Latency {latency}ms exceeded threshold of {limit}ms")

class FrameRateDropError(PerformanceError):
    """Raised when FPS falls below critical thresholds."""
    def __init__(self, fps: float, min_required: float):
        self.fps = fps
        self.min_required = min_required
        super().__init__(f"FPS drop to {fps} detected (min: {min_required})")

class ResourceLimitError(PerformanceError):
    """Raised when hardware resources are insufficient."""
    pass