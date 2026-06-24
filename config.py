import os

# Define the base configuration class
class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# Development configuration class that inherits from Config
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///{}/dev.db'.format(Config.BASE_DIR)

# Production configuration class that inherits from Config
class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URL')

# Configuration dictionary to easily access the configuration classes
CONFIG_OPTIONS = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

# Function to get the appropriate configuration class based on environment
def get_config(env):
    return CONFIG_OPTIONS.get(env, Config)
