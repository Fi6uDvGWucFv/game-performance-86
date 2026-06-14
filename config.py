import json
import os

# Default configuration values
DEFAULT_CONFIG = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fps': 60,
    'sound_enabled': True,
    'music_volume': 0.5,
    'effects_volume': 0.5
}

def load_config(file_path):
    """Load configuration from a JSON file or return defaults if the file does not exist."""
    # Check if the file exists
    if not os.path.isfile(file_path):
        return DEFAULT_CONFIG
    
    # Load the configuration file
    with open(file_path, 'r') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_CONFIG
    
    # Merge the default config with the loaded one
    merged_config = {**DEFAULT_CONFIG, **config}
    return merged_config
