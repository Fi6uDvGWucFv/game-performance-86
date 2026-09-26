import time
import logging

# Configure performance tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance-86')

class PerformanceEngine:
    def __init__(self, frame_limit: int = 60):
        self.frame_limit = frame_limit
        self.delta_time = 0.0
        self._last_tick = time.perf_counter()

    def update(self) -> float:
        """Calculates delta time for frame-rate independence."""
        current_time = time.perf_counter()
        self.delta_time = current_time - self._last_tick
        self._last_tick = current_time
        return self.delta_time

    def get_fps(self) -> float:
        """Returns current frame rate based on delta time."""
        return 1.0 / self.delta_time if self.delta_time > 0 else 0.0

def run_performance_loop(engine: PerformanceEngine):
    """Main game loop execution logic."""
    try:
        while True:
            dt = engine.update()
            fps = engine.get_fps()
            
            if fps < 30:
                logger.warning(f"Low frame rate detected: {fps:.2f} FPS")
            
            # Throttle loop to match target frame limit
            sleep_time = (1.0 / engine.frame_limit) - dt
            if sleep_time > 0:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        logger.info("Performance engine shutdown")

if __name__ == "__main__":
    engine = PerformanceEngine()
    run_performance_loop(engine)