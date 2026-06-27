class GameError(Exception):
    """Custom exception for game errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(GameError):
    """Exception raised for invalid input."""
    def __init__(self, input_value):
        message = f"Invalid input: {input_value}"
        super().__init__(message)

class OutOfBoundsError(GameError):
    """Exception raised when coordinates are out of bounds."""
    def __init__(self, x, y):
        message = f"Coordinates out of bounds: ({x}, {y})"
        super().__init__(message)

class ResourceNotFoundError(GameError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name):
        message = f"Resource not found: {resource_name}"
        super().__init__(message)