from enum import Enum

class GameLevels(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

class PlayerStats:
    MAX_HEALTH: int = 100
    MAX_LEVEL: int = 50
    BASE_DAMAGE: float = 10.0

    def __init__(self, health: int = MAX_HEALTH, level: int = 1) -> None:
        self.health: int = health
        self.level: int = level

    def is_alive(self) -> bool:
        """Check if the player is alive."""
        return self.health > 0

    def take_damage(self, amount: float) -> None:
        """Apply damage to the player."""
        if amount < 0:
            raise ValueError('Damage amount must be non-negative')
        self.health = max(self.health - amount, 0)

    def level_up(self) -> None:
        """Increase player level by 1 if below the max level."""
        if self.level < PlayerStats.MAX_LEVEL:
            self.level += 1

