import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=1):
    """Perform a GET request with retries on failure."""
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response
        except RequestException as e:
            attempt += 1
            print(f'Attempt {attempt} failed: {e}')
            if attempt < max_retries:
                time.sleep(delay)  # Wait before retrying
            else:
                print('Max retries reached. Request failed.')
                return None

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    result = retry_request(url)
    print(result)