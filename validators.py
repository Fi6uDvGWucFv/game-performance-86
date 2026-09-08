import logging

logger = logging.getLogger('game-performance-86')

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_frame_rate(fps: float) -> bool:
    """Ensures frame rate data is within realistic gaming bounds."""
    try:
        if not isinstance(fps, (int, float)):
            raise TypeError('Frame rate must be numeric')
        if fps < 0 or fps > 1000:
            raise ValueError(f'Unrealistic frame rate detected: {fps}')
        return True
    except (TypeError, ValueError) as e:
        logger.error(f'Validation failed for fps {fps}: {e}')
        return False

def validate_hardware_temp(temp: float) -> bool:
    """Checks if hardware temperature is within safe operating range."""
    try:
        if temp is None:
            raise ValidationError('Temperature reading is missing')
        if temp < -273.15:
            raise ValueError('Temperature below absolute zero')
        if temp > 150:
            logger.warning(f'Critical temperature detected: {temp}C')
        return True
    except (TypeError, ValueError, ValidationError) as e:
        logger.exception(f'Hardware monitor error: {e}')
        return False