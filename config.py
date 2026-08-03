from typing import Dict

class GameConfig:
    """
    A class to hold game configuration settings.
    """
    def __init__(self, settings: Dict[str, str]) -> None:
        """
        Initialize the GameConfig with provided settings.
        
        :param settings: A dictionary containing game settings.
        """
        self.settings = settings

    def get_setting(self, key: str) -> str:
        """
        Retrieve a specific setting by key.
        
        :param key: The key for the desired setting.
        :return: The value of the setting.
        """
        return self.settings.get(key, 'Not found')

    def set_setting(self, key: str, value: str) -> None:
        """
        Update a specific setting by key.
        
        :param key: The key for the setting to update.
        :param value: The new value for the setting.
        """
        self.settings[key] = value

    def all_settings(self) -> Dict[str, str]:
        """
        Return all settings as a dictionary.
        
        :return: A dictionary of all game settings.
        """
        return self.settings
