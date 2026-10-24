"""Custom exception classes for game performance monitoring and profiling."""

from typing import Any, Dict, Optional


class GamePerformanceError(Exception):
    """Base exception for all game performance monitoring errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: Dict[str, Any] = details or {}


class FrameRateDropError(GamePerformanceError):
    """Raised when game frame rate drops below the minimum acceptable threshold."""

    def __init__(self, current_fps: float, target_fps: float, duration_seconds: float) -> None:
        message: str = f"FPS dropped to {current_fps:.1f} (target: {target_fps:.1f}) for {duration_seconds:.2f}s"
        details: Dict[str, Any] = {
            "current_fps": current_fps,
            "target_fps": target_fps,
            "duration_seconds": duration_seconds,
        }
        super().__init__(message, details)


class MemoryThresholdExceededError(GamePerformanceError):
    """Raised when VRAM or system RAM usage exceeds the configured limit."""

    def __init__(self, memory_type: str, used_mb: float, limit_mb: float) -> None:
        message: str = f"{memory_type.upper()} usage exceeded limit: {used_mb:.1f}MB / {limit_mb:.1f}MB"
        details: Dict[str, Any] = {
            "memory_type": memory_type,
            "used_mb": used_mb,
            "limit_mb": limit_mb,
        }
        super().__init__(message, details)


class BenchmarkTimeoutError(GamePerformanceError):
    """Raised when a performance benchmark run exceeds its allocated time limit."""

    def __init__(self, benchmark_name: str, elapsed_seconds: float, max_seconds: float) -> None:
        message: str = f"Benchmark '{benchmark_name}' timed out after {elapsed_seconds:.1f}s (max: {max_seconds:.1f}s)"
        details: Dict[str, Any] = {
            "benchmark_name": benchmark_name,
            "elapsed_seconds": elapsed_seconds,
            "max_seconds": max_seconds,
        }
        super().__init__(message, details)
