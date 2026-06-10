from typing import Final

# Game constants to be used throughout the application

# Screen resolution constants
SCREEN_WIDTH: Final[int] = 1920
SCREEN_HEIGHT: Final[int] = 1080

# Frame rate constant
FPS: Final[int] = 60

# Color constants using RGB values
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game state constants
START_MENU: Final[str] = 'start_menu'
PLAYING: Final[str] = 'playing'
PAUSED: Final[str] = 'paused'
GAME_OVER: Final[str] = 'game_over'

# Other constants
MAX_PLAYERS: Final[int] = 4
MIN_PLAYERS: Final[int] = 1

