import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.RequestException as req_err:
            print(f'Request failed: {req_err}')
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts')
    return None

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as e:
        print(e)