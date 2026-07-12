import time
import requests

class NetworkError(Exception):
    pass


def retry_network_operation(url, retries=3, backoff_factor=1):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return the JSON response if successful
        except (requests.ConnectionError, requests.HTTPError) as e:
            if attempt < retries - 1:
                wait_time = backoff_factor * (2 ** attempt)  # Exponential backoff
                time.sleep(wait_time)  # Wait before the next attempt
                continue  # Retry the operation
            raise NetworkError(f"Unable to fetch data after {retries} attempts: {e}")

# Example usage
if __name__ == '__main__':
    try:
        data = retry_network_operation('https://api.example.com/data')
        print(data)
    except NetworkError as err:
        print(err)