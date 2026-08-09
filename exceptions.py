class GameError(Exception):
    """Custom exception for game errors."""
    pass

class InvalidInputError(GameError):
    """Exception raised for invalid user inputs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectivityError(GameError):
    """Exception raised for connectivity issues."""
    def __init__(self, message="Unable to connect to the server."):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameError):
    """Exception raised when resources are not found."""
    def __init__(self, resource_name):
        self.message = f'{resource_name} not found.'
        super().__init__(self.message)