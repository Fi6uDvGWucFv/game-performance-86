import logging
import json
from datetime import datetime

def setup_performance_logger(name='game-performance-86'):
    """Configures a standard logger for gaming metrics."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def log_frame_metrics(logger, frame_data: dict):
    """
    Logs telemetry data formatted as structured JSON
    to facilitate performance analysis.
    """
    metrics = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": frame_data,
        "status": "active"
    }
    try:
        # Ensure basic validation of data types before logging
        payload = json.dumps(metrics)
        logger.info(payload)
    except (TypeError, ValueError) as e:
        logger.error(f"failed to serialize frame metrics: {e}")

if __name__ == '__main__':
    perf_logger = setup_performance_logger()
    sample_data = {"fps": 144, "gpu_temp": 65, "ping_ms": 22}
    log_frame_metrics(perf_logger, sample_data)