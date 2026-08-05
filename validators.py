import re

# Validate player username requirements

def is_valid_username(username: str) -> bool:
    """Check if the username meets the criteria."""
    if not (3 <= len(username) <= 20):
        return False
    if not re.match('^[a-zA-Z0-9_]+$', username):
        return False
    return True

# Validate email format

def is_valid_email(email: str) -> bool:
    """Check if the email has a valid format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Validate password strength

def is_strong_password(password: str) -> bool:
    """Check if the password is strong enough."""
    if len(password) < 8:
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Validate game ID format

def is_valid_game_id(game_id: str) -> bool:
    """Check if the game ID format is correct."""
    return re.match('^GAME-[0-9]{4}$', game_id) is not None
