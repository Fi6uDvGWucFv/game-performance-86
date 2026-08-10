FPS_LIMIT = 60

# Standard resolution for gameplay
RESOLUTION = (1920, 1080)

# Game states
class GameState:
    MAIN_MENU = 'main_menu'
    PLAYING = 'playing'
    PAUSED = 'paused'
    GAME_OVER = 'game_over'

# Default player settings
DEFAULT_PLAYER_SETTINGS = {
    'health': 100,
    'speed': 5,
    'damage': 10,
    'armor': 1
}

# Enemy types and their attributes
ENEMY_TYPES = {
    'goblin': {'health': 30, 'damage': 5},
    'orc': {'health': 60, 'damage': 10},
    'dragon': {'health': 150, 'damage': 25}
}

# Level settings
LEVELS = [
    {'name': 'Forest', 'difficulty': 1},
    {'name': 'Cave', 'difficulty': 2},
    {'name': 'Castle', 'difficulty': 3}
]

# Key bindings
KEY_BINDINGS = {
    'move_up': 'w',
    'move_down': 's',
    'move_left': 'a',
    'move_right': 'd',
    'attack': 'space',
    'pause': 'p'
}
