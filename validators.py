import re

def is_valid_username(username):
    """Validate the username format."
    # Check for length and allowed characters
    return bool(re.match(r'^[A-Za-z0-9_]{3,25}$', username))


def is_valid_email(email):
    """Validate the email format."
    # Check for standard email format
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))


def is_valid_score(score):
    """Validate the score is a non-negative integer."
    return isinstance(score, int) and score >= 0


def validate_game_data(data):
    """Validate provided game data."
    username_valid = is_valid_username(data.get('username', ''))
    email_valid = is_valid_email(data.get('email', ''))
    score_valid = is_valid_score(data.get('score', -1))
    
    return username_valid, email_valid, score_valid
