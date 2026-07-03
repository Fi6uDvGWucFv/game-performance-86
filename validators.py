def is_valid_input(user_input):
    """
    Validates user input for the game.
    Returns True if input is valid, else False.
    """
    if not user_input:
        print("Input cannot be empty.")
        return False
    if not user_input.isalnum():
        print("Input must be alphanumeric.")
        return False
    if len(user_input) > 10:
        print("Input must be 10 characters or less.")
        return False
    return True

# Main processing loop where input validation would be applied

def main_game_loop():
    while True:
        user_input = input("Enter your command: ")
        if not is_valid_input(user_input):
            continue  # Re-prompt for valid input
        # Process valid input
        print(f"Processing command: {user_input}")
        # Break the loop (or implement game logic)
        if user_input.lower() == 'exit':
            break

if __name__ == '__main__':
    main_game_loop()