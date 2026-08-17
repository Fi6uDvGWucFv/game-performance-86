def validate_input(user_input):
    """
    Validate the user input for the game.
    Checks for empty strings and unwanted characters.
    """
    if not user_input:
        raise ValueError("Input cannot be empty.")
    if not all(c.isalnum() or c.isspace() for c in user_input):
        raise ValueError("Input must contain only alphanumeric characters and spaces.")
    return True


def get_user_input():
    """
    Get and validate user input.
    """
    while True:
        user_input = input("Enter your command: ")
        try:
            validate_input(user_input)
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}")

# Example usage in the main loop
if __name__ == '__main__':
    while True:
        command = get_user_input()
        if command.lower() == 'quit':
            break
        # Process the command
        print(f'Processing command: {command}')