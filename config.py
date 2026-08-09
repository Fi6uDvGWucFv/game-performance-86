import os

class Config:
    def __init__(self):
        # Load configuration from environment variables
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
        self.debug_mode = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
        self.max_connections = int(os.getenv('MAX_CONNECTIONS', 10))
        self.timeout = int(os.getenv('TIMEOUT', 30))

    def get_database_url(self):
        return self.database_url

    def is_debug_mode(self):
        return self.debug_mode

    def get_max_connections(self):
        return self.max_connections

    def get_timeout(self):
        return self.timeout

config = Config()