import sys
import re

class InputValidationError(Exception):
    pass

def is_valid_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError('Input must be a string.')
    if len(user_input) == 0:
        raise InputValidationError('Input cannot be empty.')
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise InputValidationError('Input contains invalid characters.')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter command: ')  # Get user input
        try:
            is_valid_input(user_input)  # Validate input
            print(f'Input accepted: {user_input}')
            # Proceed with the main logic of your game
        except InputValidationError as e:
            print(e)  # Display validation error message
        except KeyboardInterrupt:
            print('\nExiting the program.')
            sys.exit(0)  # Graceful exit

if __name__ == '__main__':
    main_processing_loop()
