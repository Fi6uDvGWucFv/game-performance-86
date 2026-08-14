class GameError(Exception):
    """Base class for all game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidInputError(GameError):
    """Exception raised for invalid input in game settings."""
    pass

class LevelNotFoundError(GameError):
    """Exception raised when a game level cannot be found."""
    def __init__(self, level_id):
        super().__init__(f'Level with ID {level_id} not found.')
        self.level_id = level_id

class PlayerNotFoundError(GameError):
    """Exception raised when a player cannot be found."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class WeaponNotEquippedError(GameError):
    """Exception raised when the action requires an equipped weapon."""
    pass

class GameStateError(GameError):
    """Exception raised for errors related to game state."""
    pass
