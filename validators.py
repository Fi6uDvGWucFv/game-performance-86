import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Failed to fetch data after {max_retries} attempts: {e}')
            time.sleep(delay)  # Wait before retrying

# Example usage:
# if __name__ == '__main__':
#     url = 'https://api.example.com/data'
#     try:
#         data = retry_request(url)
#         print(data)
#     except NetworkError as e:
#         print(e)