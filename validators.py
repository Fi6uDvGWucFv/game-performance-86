def validate_game_input(user_input):
    """Validates input for the game.

    Ensures the input is a positive integer within the
    acceptable range for game actions.
    """
    if not isinstance(user_input, int):
        raise ValueError("Input must be an integer.")
    if user_input <= 0:
        raise ValueError("Input must be a positive integer.")
    return True


def main_processing_loop():
    while True:
        try:
            user_input = int(input("Enter your action (1-10): "))
            validate_game_input(user_input)
            # Proceed with game logic using user_input
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == '__main__':
    main_processing_loop()