def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if not user_input:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input exceeds maximum length of 100 characters')
    return True

def main_loop():
    while True:
        user_input = input('Enter command: ')
        try:
            validate_input(user_input)
            process_command(user_input)
        except ValueError as e:
            print(f'Invalid input: {e}')


def process_command(command):
    print(f'Processing command: {command}')  # Placeholder for actual command processing logic