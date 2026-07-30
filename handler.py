import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameError(Exception):
    pass

class InputError(GameError):
    pass

class NetworkError(GameError):
    pass

def handle_game_action(action):
    try:
        logger.info(f'Handling action: {action}')
        if action not in ['start', 'stop', 'pause']:
            raise InputError(f'Invalid action: {action}')
        perform_action(action)
    except InputError as ie:
        logger.error(f'Input Error: {ie}')
        return json.dumps({'success': False, 'error': str(ie)})
    except NetworkError as ne:
        logger.error(f'Network Error: {ne}')
        return json.dumps({'success': False, 'error': str(ne)})
    except Exception as e:
        logger.exception('An unexpected error occurred')
        return json.dumps({'success': False, 'error': 'An unexpected error occurred'})
    return json.dumps({'success': True})

def perform_action(action):
    # Placeholder for action performance logic
    pass