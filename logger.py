import logging

class GameLogger:
    def __init__(self, name='GameLogger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._setup_handler()

    def _setup_handler(self):
        handler = logging.FileHandler('game_performance.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

if __name__ == '__main__':
    game_logger = GameLogger()
    game_logger.log_info('Game started.')
    game_logger.log_warning('Low memory warning.')
    game_logger.log_error('Error loading level.')
    game_logger.log_critical('Game crashed!')
