import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game_performance.log'),
        logging.StreamHandler()
    ]
)

def log_performance_metrics(fps, memory_usage, frame_time):
    """
    Logs game performance metrics.

    Parameters:
    fps (int): Frames per second
    memory_usage (int): Memory usage in MB
    frame_time (float): Time taken to render a frame in ms
    """
    logging.info(f'FPS: {fps}, Memory Usage: {memory_usage} MB, Frame Time: {frame_time:.2f} ms')


def log_error(message):
    """
    Logs an error message.

    Parameters:
    message (str): The error message to log
    """
    logging.error(message)


def log_warning(message):
    """
    Logs a warning message.

    Parameters:
    message (str): The warning message to log
    """
    logging.warning(message)