import enum

# Gaming performance metrics and configuration thresholds

class PerformanceTier(enum.Enum):
    ULTRA = 'ultra'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

# Frame time thresholds in milliseconds
FRAME_TIME_THRESHOLDS = {
    PerformanceTier.ULTRA: 16.6,
    PerformanceTier.HIGH: 33.3,
    PerformanceTier.MEDIUM: 50.0,
    PerformanceTier.LOW: 100.0
}

# Expected refresh rate range constants
MIN_REFRESH_RATE = 30
MAX_REFRESH_RATE = 360

# Data storage defaults
DEFAULT_SAMPLE_RATE = 60
STORAGE_FILE_EXTENSION = '.perf'

# Validation constraints for telemetry processing
MAX_LATENCY_MS = 500
MIN_CPU_USAGE_PERCENT = 0.0
MAX_CPU_USAGE_PERCENT = 100.0

def get_threshold_by_tier(tier: PerformanceTier) -> float:
    """Return frame time limit for a given performance tier."""
    return FRAME_TIME_THRESHOLDS.get(tier, 16.6)

# Configuration labels for logging
LOGGER_NAME = 'game-performance-86'
VERSION = '1.0.4'