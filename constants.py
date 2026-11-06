import os

# Performance metrics thresholds for gaming engine
MAX_FRAME_TIME_MS = 16.67
TARGET_FPS = 60

# Resource management constants
MEMORY_BUFFER_LIMIT_MB = 1024
CACHE_EXPIRATION_SECONDS = 300

# System configurations for performance tuning
DEFAULT_THREAD_POOL_SIZE = os.cpu_count() or 4
ENABLE_GPU_ACCELERATION = True

# File paths and directory structure
LOG_DIR = 'logs/performance/'
TEMP_DATA_DIR = 'tmp/cache/'

# Network timeout settings
CONNECTION_TIMEOUT_SEC = 5.0
REQUEST_RETRY_ATTEMPTS = 3

# Validation ranges
MIN_RESOLUTION_WIDTH = 800
MIN_RESOLUTION_HEIGHT = 600

def get_performance_config():
    return {
        'target_fps': TARGET_FPS,
        'max_frame_time': MAX_FRAME_TIME_MS,
        'gpu_enabled': ENABLE_GPU_ACCELERATION
    }