import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    """Attempt to make a GET request with retry logic."""
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming you want JSON data
        except requests.RequestException as e:
            if attempt == retries:
                raise NetworkError(f'Network request failed after {retries} attempts')
            else:
                print(f'Attempt {attempt} failed: {e}. Retrying in {delay} seconds...')
                time.sleep(delay)  # Wait before the next attempt
