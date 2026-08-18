import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger('GameLogger')

def log_info(message: str) -> None:
    """Logs an informational message."""
    logger.info(message)

def log_warning(message: str) -> None:
    """Logs a warning message."""
    logger.warning(message)

def log_error(message: str) -> None:
    """Logs an error message."""
    logger.error(message)

def log_debug(message: str) -> None:
    """Logs a debug message."""
    logger.debug(message)

def log_exception(message: str) -> None:
    """Logs an exception message with stack trace."""
    logger.exception(message)