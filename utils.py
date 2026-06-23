import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=1):
    """Attempts to send a GET request to the given URL with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                print(f'Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...')
                time.sleep(delay)
            else:
                raise NetworkError(f'Failed to fetch data after {retries} attempts') from e
