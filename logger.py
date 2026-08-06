import logging

# Configure logging settings
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger for the game
logger = logging.getLogger('game_logger')

def log_info(message):
    """Log information messages."""
    logger.info(message)


def log_warning(message):
    """Log warning messages."""
    logger.warning(message)


def log_error(message):
    """Log error messages."""
    logger.error(message)


def log_debug(message):
    """Log debug messages, useful during development."""
    logger.debug(message)


def log_game_event(event_type, event_details):
    """Log game events with type and details."""
    logger.info(f'Event Type: {event_type}, Event Details: {event_details}')

# Example usage
if __name__ == '__main__':
    log_info('Game started')
    log_warning('Low health warning')
    log_error('Player connection lost')
    log_debug('Debugging player input')
    log_game_event('Score Update', {'player': 'Player1', 'score': 100})