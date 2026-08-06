import random
import time

class GameHelper:
    def __init__(self):
        pass

    @staticmethod
    def generate_random_number(min_value: int, max_value: int) -> int:
        """Generate a random integer within a specific range."""
        return random.randint(min_value, max_value)
    
    @staticmethod
    def wait(seconds: int) -> None:
        """Pause execution for a specified number of seconds."""
        time.sleep(seconds)
    
    @staticmethod
    def format_score(score: int) -> str:
        """Format the score for display."""
        return f'Score: {score}'
    
    @staticmethod
    def is_game_over(lives: int) -> bool:
        """Check if the game is over based on lives."""
        return lives <= 0

# Example usage
if __name__ == '__main__':
    helper = GameHelper()
    random_number = helper.generate_random_number(1, 100)
    print(f'Generated random number: {random_number}')
    helper.wait(2)
    print(helper.format_score(42))
    print('Game over:', helper.is_game_over(0))