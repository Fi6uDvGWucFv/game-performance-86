import re

class InputValidationError(Exception):
    pass

def validate_username(username):
    if not re.match('^[a-zA-Z0-9_]{3,20}$', username):
        raise InputValidationError('Username must be 3-20 characters long and can only contain letters, digits, and underscores.')


def validate_score(score):
    if not isinstance(score, int) or score < 0:
        raise InputValidationError('Score must be a non-negative integer.')


def validate_game_input(username, score):
    validate_username(username)
    validate_score(score)

