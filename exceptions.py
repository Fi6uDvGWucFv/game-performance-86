from typing import Optional

class PerformanceError(Exception):
    """Base exception for all performance monitoring issues."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class FrameRateDropError(PerformanceError):
    """Raised when the frame rate falls below the threshold."""
    pass

class ResourceLeakError(PerformanceError):
    """Raised when memory or CPU usage exceeds safe bounds."""
    pass

class ConfigurationError(PerformanceError):
    """Raised when the performance profile is invalid."""
    pass

def format_error(error: PerformanceError) -> str:
    """Format a PerformanceError for logging purposes."""
    code_str = f"[{error.code}] " if error.code else ""
    return f"Performance issue detected: {code_str}{str(error)}"