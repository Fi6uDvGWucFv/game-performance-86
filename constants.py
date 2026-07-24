FPS_TARGET = 60

# Color constants
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
GRAVITY = 9.81  # Acceleration due to gravity in m/s^2
FPS_TO_MS = 1000 / FPS_TARGET  # Convert frames per second to milliseconds

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player constants
PLAYER_SPEED = 5
PLAYER_JUMP_HEIGHT = 15

# Level constants
LEVEL_COUNT = 5
LEVEL_DIFFICULTY = {'easy': 1, 'medium': 2, 'hard': 3}
