from typing import List, Dict

def calculate_average(scores: List[int]) -> float:
    """
    Calculate the average of a list of scores.

    Args:
        scores (List[int]): A list of integer scores.

    Returns:
        float: The average score.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def format_scoreboard(scores: Dict[str, int]) -> str:
    """
    Format a scoreboard dictionary into a string.

    Args:
        scores (Dict[str, int]): A dictionary with player names as keys and their scores as values.

    Returns:
        str: A formatted string of scores.
    """
    formatted_scores = [f'{player}: {score}' for player, score in scores.items()]
    return '\n'.join(formatted_scores)


def find_top_scorer(scores: Dict[str, int]) -> str:
    """
    Identify the player with the highest score.

    Args:
        scores (Dict[str, int]): A dictionary with player names as keys and their scores as values.

    Returns:
        str: The name of the top scorer.
    """
    if not scores:
        return "No players in the scoreboard."
    return max(scores, key=scores.get)