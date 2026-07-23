class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InvalidMoveError(GameError):
    """Exception raised for invalid moves."""
    def __init__(self, move):
        self.move = move
        super().__init__(f'Invalid move: {self.move}')

class ResourceNotFoundError(GameError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name):
        self.resource_name = resource_name
        super().__init__(f'Resource not found: {self.resource_name}')

class InsufficientResourcesError(GameError):
    """Exception raised for insufficient resources."""
    def __init__(self, required, available):
        self.required = required
        self.available = available
        super().__init__(f'Insufficient resources: required {self.required}, available {self.available}')

# Example usage in a game function:

def make_move(move, resources):
    allowed_moves = ['up', 'down', 'left', 'right']
    if move not in allowed_moves:
        raise InvalidMoveError(move)
    if resources < 1:
        raise InsufficientResourcesError(1, resources)
    # Proceed with making the move