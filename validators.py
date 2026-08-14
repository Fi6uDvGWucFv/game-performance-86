def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be a number.')
    if score < 0:
        raise ValueError('Score cannot be negative.')
    return True

def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string.')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters.')
    return True

if __name__ == '__main__':
    try:
        validate_score(10)
        validate_username('player1')
    except ValueError as e:
        print(f'Validation error: {e}')