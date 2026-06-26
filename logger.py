import logging

class GameLogger:
    """
    A simple logger class for gaming applications.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the GameLogger with a specific name.

        :param name: The name of the logger.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """
        Logs a message with DEBUG level.

        :param message: The message to log.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs a message with INFO level.

        :param message: The message to log.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a message with WARNING level.

        :param message: The message to log.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs a message with ERROR level.

        :param message: The message to log.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a message with CRITICAL level.

        :param message: The message to log.
        """
        self.logger.critical(message)