import time
from collections import deque
import math

def calculate_fps(last_time: float, current_time: float = None) -> float:
    """Calculate instantaneous FPS from time delta."""
    if current_time is None:
        current_time = time.time()
    delta = current_time - last_time
    if delta <= 0:
        return 0.0
    return 1.0 / delta

def update_fps_history(history: deque, fps: float, max_size: int = 60) -> None:
    """Append FPS value to history deque, limit size."""
    history.append(fps)
    if len(history) > max_size:
        history.popleft()

def get_average_fps(history: deque) -> float:
    """Compute average FPS from deque history."""
    if len(history) == 0:
        return 0.0
    return sum(history) / len(history)

def is_performance_poor(avg_fps: float, threshold: float = 30.0) -> bool:
    """Determine if average FPS indicates poor performance."""
    return 0 < avg_fps < threshold

def frame_time_ms(fps: float) -> float:
    """Convert FPS to milliseconds per frame."""
    if fps <= 0:
        return 0.0
    return 1000.0 / fps

def normalize_coords(x: float, y: float, max_x: float, max_y: float) -> tuple[float, float]:
    """Scale coordinates to [0, 1] range."""
    if max_x <= 0 or max_y <= 0:
        return (0.0, 0.0)
    return (x / max_x, y / max_y)

def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate distance between points."""
    return math.hypot(x2 - x1, y2 - y1)

def clamp_to_range(value: float, minimum: float, maximum: float) -> float:
    """Restrict value to specified range."""
    return max(minimum, min(value, maximum))

if __name__ == "__main__":
    history = deque(maxlen=60)
    last = time.time()
    for i in range(5):
        time.sleep(0.033)  # approx 30 fps
        now = time.time()
        fps = calculate_fps(last, now)
        update_fps_history(history, fps)
        last = now
    avg_fps = get_average_fps(history)
    print(f"Avg FPS: {avg_fps:.2f}")
    print(f"Poor perf: {is_performance_poor(avg_fps)}")
    print(f"Frame time: {frame_time_ms(avg_fps):.2f} ms")