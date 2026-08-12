import json
import logging

logger = logging.getLogger(__name__)

class GameHandler:
    def __init__(self, game_data):
        self.game_data = game_data
        self.score = 0
        self.level = 1

    def update_score(self, points):
        self.score += points
        logger.info(f'Score updated: {self.score}')

    def level_up(self):
        self.level += 1
        logger.info(f'Level increased to: {self.level}')

    def save_game(self, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(self.game_data, file)
                logger.info('Game saved successfully')
        except Exception as e:
            logger.error(f'Error saving game: {e}')

    def load_game(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.game_data = json.load(file)
                logger.info('Game loaded successfully')
        except Exception as e:
            logger.error(f'Error loading game: {e}')