from typing import List, Dict, Any

class GameHandler:
    """
    A class to handle game-related operations.
    """

    def __init__(self, game_name: str, high_score: int = 0) -> None:
        """
        Initializes the GameHandler with a game name and high score.
        """
        self.game_name: str = game_name
        self.high_score: int = high_score

    def update_high_score(self, new_score: int) -> None:
        """
        Updates the high score if the new score is higher.
        """
        if new_score > self.high_score:
            print(f"Updating high score from {self.high_score} to {new_score}")
            self.high_score = new_score
        else:
            print(f"New score {new_score} does not exceed high score {self.high_score}")

    def get_game_info(self) -> Dict[str, Any]:
        """
        Returns a dictionary with game information.
        """
        return {
            'game_name': self.game_name,
            'high_score': self.high_score
        }

    def display_high_score(self) -> None:
        """
        Displays the current high score.
        """
        print(f"Current high score for {self.game_name}: {self.high_score}")

if __name__ == '__main__':
    game = GameHandler('Space Invaders')
    game.update_high_score(100)
    game.display_high_score()
    game.update_high_score(80)
    game.display_high_score()
    info = game.get_game_info()
    print(info)