import logging
import sys
from datetime import datetime

# Configure logging for game-performance-86 diagnostics
logger = logging.getLogger('game_perf')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Stream handler for console output
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def format_performance_metric(metric_name: str, value: float, threshold: float) -> str:
    """Formats performance metrics with warning status if threshold exceeded."""
    status = "CRITICAL" if value > threshold else "OK"
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    
    return f"[{timestamp}] {status} | {metric_name}: {value:.2f}ms (Limit: {threshold}ms)"

def log_frame_time(frame_ms: float, budget: float = 16.67):
    """Logs frame timing data to standard output."""
    message = format_performance_metric("FrameTime", frame_ms, budget)
    if frame_ms > budget:
        logger.warning(message)
    else:
        logger.info(message)

if __name__ == '__main__':
    # Example usage for performance testing
    log_frame_time(12.5, 16.67)
    log_frame_time(22.1, 16.67)