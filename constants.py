MAX_FPS = 60

# Game screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors in RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game state constants
GAME_RUNNING = 'running'
GAME_PAUSED = 'paused'
GAME_OVER = 'game_over'

# Physics constants
GRAVITY = 9.81
JUMP_VELOCITY = 10

# Player settings
PLAYER_SPEED = 5
PLAYER_HEALTH = 100

# Asset paths
def get_asset_path(asset_name):
    import os
    return os.path.join('assets', asset_name)

# Example asset paths
PLAYER_SPRITE = get_asset_path('player_sprite.png')
ENEMY_SPRITE = get_asset_path('enemy_sprite.png')