import logging

# Configure the logger for the game performance module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GameLogger:
    """A simple logger for game performance monitoring."""
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, msg):
        """Log a debug message"""
        self.logger.debug(msg)

    def info(self, msg):
        """Log an info message"""
        self.logger.info(msg)

    def warning(self, msg):
        """Log a warning message"""
        self.logger.warning(msg)

    def error(self, msg):
        """Log an error message"""
        self.logger.error(msg)

    def critical(self, msg):
        """Log a critical message"""
        self.logger.critical(msg)

# Create a global logger instance for the module
logger = GameLogger('GamePerformanceLogger')