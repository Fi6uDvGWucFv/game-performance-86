import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("game_performance.utils")

def retry_network_op(
    max_retries: int = 3,
    initial_backoff: float = 0.5,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """
    Decorator to retry network-sensitive operations (such as telemetry submissions
    and matchmaking pings) using exponential backoff and jitter.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_backoff
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        logger.error(
                            f"Failed network operation '{func.__name__}' "
                            f"after {max_retries} attempts: {e}"
                        )
                        raise e

                    current_delay = delay
                    if jitter:
                        current_delay = random.uniform(delay * 0.5, delay * 1.5)

                    logger.warning(
                        f"Network operation '{func.__name__}' failed ({e}). "
                        f"Retrying in {current_delay:.2f}s (Attempt {attempt}/{max_retries})..."
                    )
                    time.sleep(current_delay)
                    delay *= backoff_factor
        return wrapper
    return decorator