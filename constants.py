from typing import Final, Dict, List

# Configuration for performance monitoring thresholds
MAX_FRAME_TIME_MS: Final[float] = 16.67
WARNING_FRAME_TIME_MS: Final[float] = 33.33

# Standardized metric identifiers for telemetry
METRIC_FPS: Final[str] = "fps"
METRIC_LATENCY: Final[str] = "latency_ms"
METRIC_MEMORY: Final[str] = "memory_mb"

# Supported gaming hardware categories
SUPPORTED_PLATFORMS: Final[List[str]] = ["windows", "linux", "macos", "console"]

# Error code mappings for engine diagnostics
DIAGNOSTIC_CODES: Final[Dict[int, str]] = {
    1001: "Insufficient system memory",
    1002: "GPU driver timeout",
    1003: "Frame drop threshold exceeded",
    1004: "Network packet jitter high"
}

# Default performance sampling interval in seconds
DEFAULT_SAMPLING_RATE: Final[float] = 0.5

# Internal naming conventions for reporting
NAMESPACE_PREFIX: Final[str] = "game_perf_86"