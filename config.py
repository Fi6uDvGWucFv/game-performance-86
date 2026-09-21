import os
import logging
from typing import Any, Dict

# Configure logging for performance tracking
logger = logging.getLogger('game-performance-86')

class ConfigError(Exception):
    """Custom exception for configuration failures."""
    pass

def load_performance_settings(path: str) -> Dict[str, Any]:
    """Loads and validates configuration from environment or file."""
    if not path or not os.path.exists(path):
        logger.error(f"configuration file missing: {path}")
        raise ConfigError("invalid path provided")

    try:
        with open(path, 'r') as f:
            data = f.read()
            if not data.strip():
                raise ValueError("empty file content")
            
            # Simulate parsing logic
            import json
            settings = json.loads(data)
            
            # Ensure mandatory keys exist for game engine
            required = ['refresh_rate', 'texture_quality']
            for key in required:
                if key not in settings:
                    raise KeyError(f"missing required config: {key}")
            
            return settings

    except (json.JSONDecodeError, ValueError, KeyError) as e:
        logger.error(f"config parsing failure: {e}")
        raise ConfigError(f"configuration load failure: {e}")
    except Exception as e:
        logger.critical(f"unexpected system error: {e}")
        raise ConfigError("unhandled configuration exception")