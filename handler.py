from typing import Any, Dict, List


def process_game_event(event: Dict[str, Any]) -> None:
    """
    Process a gaming event to update the game state.

    Parameters:
    event (Dict[str, Any]): A dictionary containing game event data.
    """
    if event['type'] == 'player_joined':
        handle_player_joined(event['data'])
    elif event['type'] == 'player_left':
        handle_player_left(event['data'])
    elif event['type'] == 'game_action':
        handle_game_action(event['data'])
    else:
        print(f'Unknown event type: {event['type']}')


def handle_player_joined(data: Dict[str, Any]) -> None:
    """
    Handle a player joining the game.

    Parameters:
    data (Dict[str, Any]): Information about the player.
    """
    print(f'Player joined: {data['player_id']}')


def handle_player_left(data: Dict[str, Any]) -> None:
    """
    Handle a player leaving the game.

    Parameters:
    data (Dict[str, Any]): Information about the player.
    """
    print(f'Player left: {data['player_id']}')


def handle_game_action(data: Dict[str, Any]) -> None:
    """
    Handle a game action taken by a player.

    Parameters:
    data (Dict[str, Any]): Action data including player ID and action details.
    """
    print(f'Player {data['player_id']} performed action: {data['action']}')
