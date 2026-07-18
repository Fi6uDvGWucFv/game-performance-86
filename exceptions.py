class GameError(Exception):
    """Base class for game-related exceptions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class InvalidInputError(GameError):
    """Exception raised for invalid player input."""
    def __init__(self, message: str = 'Invalid input provided.') -> None:
        super().__init__(message)

class GameNotFoundError(GameError):
    """Exception raised when the game is not found."""
    def __init__(self, game_name: str) -> None:
        message = f'Game not found: {game_name}'
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_id: str) -> None:
        message = f'Player not found with ID: {player_id}'
        super().__init__(message)
