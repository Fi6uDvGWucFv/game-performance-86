from typing import List

class Game:
    def __init__(self, name: str, players: List[str]) -> None:
        """Initializes a new game.

        Args:
            name (str): The name of the game.
            players (List[str]): A list of player names.
        """
        self.name = name
        self.players = players

    def start(self) -> None:
        """Starts the game and announces the players."""
        print(f'Starting game: {self.name}')
        print('Players in this game:')
        for player in self.players:
            print(f'- {player}')

    def add_player(self, player: str) -> None:
        """Adds a player to the game.

        Args:
            player (str): The name of the player to add.
        """
        self.players.append(player)

    def get_player_count(self) -> int:
        """Returns the number of players in the game.

        Returns:
            int: The current player count.
        """
        return len(self.players)

if __name__ == '__main__':
    game = Game('Battle Royale', ['Alice', 'Bob'])
    game.start()
    game.add_player('Charlie')
    print(f'Total players: {game.get_player_count()}')