import re

# A collection of validation functions for the game

def is_valid_username(username):
    """Check if the username is valid."
    # Username must be alphanumeric and 3-15 characters long.
    return bool(re.match('^[a-zA-Z0-9]{3,15}$', username))


def is_valid_email(email):
    """Check if the email format is valid."
    # Basic regex for validating an email.
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))


def is_valid_score(score):
    """Check if the score is a non-negative integer."
    # Score must be a non-negative integer.
    return isinstance(score, int) and score >= 0


def is_valid_game_id(game_id):
    """Check if the game ID is formatted correctly."
    # Game ID must be a UUID.
    uuid_regex = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    return bool(re.match(uuid_regex, game_id))

# Example validation use cases
if __name__ == '__main__':
    print(is_valid_username('player1'))  # True
    print(is_valid_email('test@example.com'))  # True
    print(is_valid_score(100))  # True
    print(is_valid_game_id('123e4567-e89b-12d3-a456-426614174000'))  # True