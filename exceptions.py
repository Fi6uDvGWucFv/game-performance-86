class GameError(Exception):
    """
    Custom exception for game-related errors.
    """
    pass

class InvalidInputError(GameError):
    """
    Raised when user input is invalid.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NotFoundError(GameError):
    """
    Raised when an entity is not found.
    """
    def __init__(self, entity: str) -> None:
        message = f"{entity} not found."
        super().__init__(message)

class PermissionDeniedError(GameError):
    """
    Raised when permission is denied.
    """
    def __init__(self, action: str) -> None:
        message = f"Permission denied for action: {action}."
        super().__init__(message)