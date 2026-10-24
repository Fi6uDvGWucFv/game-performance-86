from typing import Dict, Final

# Standardized gaming telemetry categories
GAME_METRICS_SCHEMA: Final[Dict[str, str]] = {
    "fps": "float",
    "frame_time_ms": "float",
    "gpu_temp_c": "int",
    "cpu_usage_pct": "float",
    "ram_usage_mb": "int",
    "network_latency_ms": "int",
    "gpu_utilization_pct": "int"
}

# Performance thresholds for performance monitoring
PERF_THRESHOLDS: Final[Dict[str, float]] = {
    "min_fps": 60.0,
    "max_frame_time_ms": 16.6,
    "max_gpu_temp": 85.0,
    "alert_latency_ms": 100.0
}

# Configuration for telemetry sampling
TELEMETRY_SETTINGS: Final[Dict[str, int]] = {
    "buffer_size": 1024,
    "sample_interval_ms": 500,
    "retry_attempts": 3
}

def get_metric_type(metric_name: str) -> str:
    """Returns the data type string for a given metric."""
    return GAME_METRICS_SCHEMA.get(metric_name, "float")

def is_within_limits(metric: str, value: float) -> bool:
    """Checks if a metric value stays under warning limits."""
    if "temp" in metric:
        return value <= PERF_THRESHOLDS["max_gpu_temp"]
    if metric == "frame_time_ms":
        return value <= PERF_THRESHOLDS["max_frame_time_ms"]
    return True