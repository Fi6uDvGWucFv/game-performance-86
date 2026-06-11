import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Example usage
if __name__ == '__main__':
    log = Logger(__name__)
    log.info('This is an info message')
    log.error('This is an error message')