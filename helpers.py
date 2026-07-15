import random
import numpy as np

def calculate_average(scores):
    """
    Calculate the average score from a list of scores.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def generate_random_id(length=8):
    """
    Generate a random alphanumeric string as an ID.
    """  
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


def normalize_vector(vector):
    """
    Normalize a numerical vector to unit length.
    """ 
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def clamp(value, min_value, max_value):
    """
    Clamp a value between min_value and max_value.
    """  
    return max(min(value, max_value), min_value)
