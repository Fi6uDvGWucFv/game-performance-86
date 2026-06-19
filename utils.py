import random
import numpy as np


def generate_random_points(num_points, x_range, y_range):
    """Generate a list of random points within specified ranges."""
    points = []
    for _ in range(num_points):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        points.append((x, y))
    return points


def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clamp(value, min_value, max_value):
    """Clamp the value to be within min_value and max_value."""
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    """Linearly interpolate between start and end by t."""
    return start + (end - start) * t


def random_choice(choices):
    """Return a random choice from a list."""
    return random.choice(choices)