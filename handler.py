import sys

class GameInputHandler:
    def __init__(self):
        self.valid_commands = {'move', 'attack', 'defend', 'quit'}

    def get_user_input(self):
        command = input('Enter command: ').strip().lower()
        return command

    def validate_input(self, command):
        if command not in self.valid_commands:
            print(f'Invalid command: {command}')
            return False
        return True

    def process_commands(self):
        while True:
            command = self.get_user_input()
            if command == 'quit':
                print('Exiting game...')
                sys.exit()
            if self.validate_input(command):
                self.execute_command(command)

    def execute_command(self, command):
        print(f'Executing command: {command}')

if __name__ == '__main__':
    input_handler = GameInputHandler()
    input_handler.process_commands()