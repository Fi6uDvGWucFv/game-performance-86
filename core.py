import random
import string

# Constants for user input validation
MIN_LENGTH = 3
MAX_LENGTH = 15

# Function to validate input for player names
def validate_player_name(name):
    if not (MIN_LENGTH <= len(name) <= MAX_LENGTH):
        raise ValueError(f'Name must be between {MIN_LENGTH} and {MAX_LENGTH} characters.')
    if not name.isalnum():
        raise ValueError('Name must contain only alphanumeric characters.')
    return True

# Main processing loop for the game
def main_loop():
    players = []
    while True:
        try:
            player_name = input('Enter player name (or type 