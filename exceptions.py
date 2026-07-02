class GameError(Exception):
    """Base class for exceptions in the gaming module."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class InvalidPlayerNameError(GameError):
    """Exception raised for invalid player name errors."""
    def __init__(self, player_name: str) -> None:
        message = f"Invalid player name: '{player_name}'."
        super().__init__(message)
        self.player_name = player_name

class OutOfBoundsError(GameError):
    """Exception raised when a game action goes out of bounds."""
    def __init__(self, action: str) -> None:
        message = f"Action '{action}' is out of game bounds."
        super().__init__(message)
        self.action = action

class GameNotFoundError(GameError):
    """Exception raised when the specified game is not found."""
    def __init__(self, game_id: int) -> None:
        message = f"Game with ID {game_id} not found."
        super().__init__(message)
        self.game_id = game_id
