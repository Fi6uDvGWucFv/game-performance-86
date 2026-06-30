import time
import random

class NetworkError(Exception):
    pass

def simulate_network_operation():
    if random.random() < 0.7:
        raise NetworkError("Network operation failed")
    return "Success"

def retry(max_retries=5, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    print(f'Attempt {attempt + 1} failed: {e}')
                    time.sleep(delay)
            raise NetworkError("Max retries exceeded")
        return wrapper
    return decorator

@retry(max_retries=3, delay=1)
def network_request():
    return simulate_network_operation()

if __name__ == '__main__':
    try:
        result = network_request()
        print(result)
    except NetworkError as e:
        print(f'Final error: {e}')