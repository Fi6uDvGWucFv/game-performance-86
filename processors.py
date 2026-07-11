import re

class InputValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise InputValidationError('Username must be a string.')
    if len(username) < 3 or len(username) > 20:
        raise InputValidationError('Username must be between 3 and 20 characters.')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise InputValidationError('Username can only contain alphanumeric characters and underscores.')


def main_processing_loop():
    while True:
        user_input = input('Enter your username: ')
        try:
            validate_username(user_input)
            print(f'Valid username: {user_input}')
            break  # Exit the loop on valid input
        except InputValidationError as e:
            print(e)  # Print validation error and prompt again


if __name__ == '__main__':
    main_processing_loop()