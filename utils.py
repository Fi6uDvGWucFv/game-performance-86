import time

def time_execution(func):
    """Decorator to time the execution of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@time_execution
def optimize_performance(data):
    """Optimizes game performance by filtering unnecessary data."""
    filtered_data = [d for d in data if d.is_valid()]
    return filtered_data

@time_execution
def calculate_frame_rate(frames, time_elapsed):
    """Calculates the frame rate based on frames rendered and time elapsed."""
    if time_elapsed > 0:
        return frames / time_elapsed
    return 0
