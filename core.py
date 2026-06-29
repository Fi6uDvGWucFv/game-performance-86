import random
from typing import List, Tuple, Optional

class Game:
    def __init__(self, name: str, max_players: int) -> None:
        self.name = name
        self.max_players = max_players
        self.players: List[str] = []

    def add_player(self, player: str) -> Optional[str]:
        if len(self.players) < self.max_players:
            self.players.append(player)
            return f'Player {player} added.'
        return 'Cannot add player; max players reached.'

    def start_game(self) -> str:
        if len(self.players) == 0:
            return 'No players to start the game.'
        return f'Game {self.name} started with players: {self.players}'

    def get_winner(self) -> str:
        if len(self.players) == 0:
            return 'No players to determine a winner.'
        winner = random.choice(self.players)
        return f'The winner is {winner}!'

if __name__ == '__main__':
    game = Game('Adventure Quest', 4)
    print(game.add_player('Alice'))
    print(game.add_player('Bob'))
    print(game.start_game())
    print(game.get_winner())