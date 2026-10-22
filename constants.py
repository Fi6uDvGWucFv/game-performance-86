import multiprocessing

# hardware-level optimization thresholds for gaming engine
MAX_FRAME_BUFFER_SIZE = 144
TARGET_TICK_RATE = 60

# memory allocation management constants
CHUNK_SIZE_BYTES = 1024 * 64
CACHE_EXPIRY_SECONDS = 300

# threading optimization for core workload balancing
CORE_COUNT = multiprocessing.cpu_count()
WORKER_THREAD_POOL_SIZE = max(4, CORE_COUNT * 2)

# network throughput tuning constants
PACKET_BUFFER_LIMIT = 2048
SOCKET_TIMEOUT_MS = 500

# performance flag settings
ENABLE_PREFETCH = True
USE_FAST_MATH = True

# gpu acceleration parameters
TEXTURE_COMPRESSION_LEVEL = 2
BATCH_RENDER_LIMIT = 500