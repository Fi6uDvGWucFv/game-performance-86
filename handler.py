import random

class GameHandler:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0

    def start_game(self):
        print(f'Welcome {self.player_name}! Let the game begin!')
        self.play_rounds(5)

    def play_rounds(self, rounds):
        for _ in range(rounds):
            self.play_round()
        print(f'Final Score: {self.score}')

    def play_round(self):
        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            self.score += 10
            print(f'You won this round! Current Score: {self.score}')
        else:
            print('You lost this round.')

if __name__ == '__main__':
    player = GameHandler('Player1')
    player.start_game()