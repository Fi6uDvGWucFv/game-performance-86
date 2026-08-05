def safe_divide(numerator, denominator):
    """Safely divides two numbers, handling division by zero."""
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 'Error: Division by zero'
    except TypeError:
        return 'Error: Invalid input types, please provide numbers'
    return result


def read_file(file_path):
    """Reads a file and returns its contents, with error handling."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'Error: File not found'
    except IOError:
        return 'Error: An error occurred while reading the file'


def calculate_average(numbers):
    """Calculates the average of a list of numbers, with error handling."""
    if not numbers:
        return 'Error: List is empty'
    try:
        average = sum(numbers) / len(numbers)
    except TypeError:
        return 'Error: List must contain only numbers'
    return average


def connect_to_game_server(server_address):
    """Simulates connecting to a game server with error handling."""
    try:
        if not isinstance(server_address, str) or not server_address:
            raise ValueError('Invalid server address')
        # Simulate connection logic here
        return 'Connected to server: ' + server_address
    except ValueError as ve:
        return f'Error: {ve}'
    except Exception as e:
        return f'Error: An unexpected error occurred - {e}'