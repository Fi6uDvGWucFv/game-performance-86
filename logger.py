import logging
from logging.handlers import RotatingFileHandler
import os

def setup_game_logger(name: str = 'game_performance_86', log_file: str = 'game.log'):
    """Initializes a rotating logger for performance tracking."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        os.path.join('logs', log_file),
        maxBytes=5*1024*1024,
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger

# Logger instance for game engine performance metrics
performance_logger = setup_game_logger()