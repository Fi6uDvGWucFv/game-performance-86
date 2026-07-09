def validate_user_input(input_value):
    """
    Validates user input for the game.
    
    Args:
        input_value (str): The user input to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(input_value, str):
        return False
    input_value = input_value.strip()
    if not input_value:
        return False
    if len(input_value) > 20:
        return False
    return True


def main_game_loop():
    game_running = True
    while game_running:
        user_input = input("Enter your command: ")
        if validate_user_input(user_input):
            # Process the valid command
            print(f'Processing command: {user_input}')
        else:
            print("Invalid input, please try again.")


if __name__ == '__main__':
    main_game_loop()