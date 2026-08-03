import random
import math

def calculate_distance(point_a, point_b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def generate_random_position(area_width, area_height):
    """Generate a random position within the specified area."""
    x = random.randint(0, area_width)
    y = random.randint(0, area_height)
    return (x, y)


def is_within_bounds(position, area_width, area_height):
    """Check if the position is within the given bounds."""
    return 0 <= position[0] <= area_width and 0 <= position[1] <= area_height


def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum limit."""
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    """Linearly interpolate between two values."""
    return (1 - t) * start + t * end


def normalize(vector):
    """Normalize a vector to have a magnitude of 1."""
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)