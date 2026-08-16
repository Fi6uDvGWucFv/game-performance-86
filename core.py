import random

class Game:
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)
            return True
        return False

    def start(self):
        if len(self.players) == self.max_players:
            print(f'Starting game: {self.name}')
            return True
        print('Not enough players to start the game.')
        return False

    def generate_random_number(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def show_players(self):
        return self.players

# Example usage
if __name__ == '__main__':
    game = Game('Mystery Dungeon', 4)
    game.add_player('Alice')
    game.add_player('Bob')
    game.add_player('Charlie')
    game.add_player('Diana')
    game.start()
    print('Players in the game:', game.show_players())
    print('Random number generated:', game.generate_random_number(1, 100))