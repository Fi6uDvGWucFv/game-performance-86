def is_positive_integer(value):
    """
    Check if the value is a positive integer.
    """
    return isinstance(value, int) and value > 0


def is_non_empty_string(value):
    """
    Check if the value is a non-empty string.
    """
    return isinstance(value, str) and bool(value.strip())


def is_valid_email(email):
    """
    Validate the email format using a regex pattern.
    """
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_in_range(value, min_value, max_value):
    """
    Check if the value is within a specified range.
    """
    return isinstance(value, (int, float)) and min_value <= value <= max_value


def is_valid_game_rating(rating):
    """
    Validate the game rating between 0 and 10.
    """
    return is_in_range(rating, 0, 10)