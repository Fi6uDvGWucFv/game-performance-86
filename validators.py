import re

def is_valid_username(username: str) -> bool:
    '''Validate the username for gaming accounts. Must be 3-15 characters long and alphanumeric.'''  
    if not (3 <= len(username) <= 15):
        return False
    return bool(re.match('^[A-Za-z0-9]+$', username))


def is_valid_email(email: str) -> bool:
    '''Validate the email format for gaming accounts.'''  
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def is_valid_password(password: str) -> bool:
    '''Validate the password. Must be at least 8 characters with at least one uppercase letter, one lowercase letter, one number, and one special character.'''  
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
