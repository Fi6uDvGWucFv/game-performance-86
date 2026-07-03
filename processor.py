import time
import requests
from requests.exceptions import RequestException


def retry_request(url, max_retries=3, backoff_factor=0.5):
    """Perform a network request with retry logic."""
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # raise error for bad responses
            return response.json()  # assuming we expect a JSON response
        except RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait_time)  # wait before retrying
            print(f'Retry {retries}/{max_retries} for {url} due to {e}')  # log retry
    raise Exception(f'Max retries exceeded for {url}')

# Example usage:
# result = retry_request('http://example.com/api/data')
