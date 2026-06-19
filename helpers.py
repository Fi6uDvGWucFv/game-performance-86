import random
import math

# Generate a random float within a range

def random_float(min_val: float, max_val: float) -> float:
    """Returns a random float between min_val and max_val."""
    return random.uniform(min_val, max_val)

# Calculate distance between two points

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Clamp a value within a minimum and maximum

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamps value to be within the min_val and max_val range."""
    return max(min_val, min(value, max_val))

# Generate a random integer within a specified range

def random_int(min_val: int, max_val: int) -> int:
    """Returns a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

# Check if a number is even

def is_even(number: int) -> bool:
    """Returns True if the number is even, else False."""
    return number % 2 == 0