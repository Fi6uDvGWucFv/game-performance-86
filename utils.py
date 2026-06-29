import time

def timed_function(func):
    """Decorator to time a function's execution."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timed_function
def compute_heavy_operation(data):
    """Simulates a heavy computation on data."""
    total = 0
    for num in data:
        total += num ** 2  # Example computation
    return total

@timed_function
def process_game_data(game_data):
    """Processes the game data to optimize performance."""
    optimized_data = [data.lower() for data in game_data if isinstance(data, str)]
    return optimized_data
