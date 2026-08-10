class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class ResourceNotFoundError(GameError):
    """Exception raised when a requested resource is not found."""
    def __init__(self, resource_name):
        self.resource_name = resource_name
        super().__init__(f'Resource not found: {resource_name}')

class InvalidMoveError(GameError):
    """Exception raised for invalid moves in the game."""
    def __init__(self, move, reason):
        self.move = move
        self.reason = reason
        super().__init__(f'Invalid move: {move} - {reason}')

class GameNotInitializedError(GameError):
    """Exception raised when the game is not initialized properly."""
    def __init__(self):
        super().__init__('Game has not been initialized.')

# Example usage in the game:
# raise ResourceNotFoundError('player_1')
# raise InvalidMoveError('move_left', 'out of bounds')
# raise GameNotInitializedError()