from typing import List, Dict


def calculate_average(scores: List[int]) -> float:
    """
    Calculate the average of a list of scores.

    Parameters:
    scores (List[int]): A list of integer scores.

    Returns:
    float: The average score.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def find_top_scorers(scores: Dict[str, int], threshold: int) -> List[str]:
    """
    Find players who scored above a certain threshold.

    Parameters:
    scores (Dict[str, int]): A dictionary mapping player names to their scores.
    threshold (int): The score threshold to filter players.

    Returns:
    List[str]: A list of player names who scored above the threshold.
    """
    return [player for player, score in scores.items() if score > threshold]


def format_scoreboard(scores: Dict[str, int]) -> str:
    """
    Format the scoreboard as a string.

    Parameters:
    scores (Dict[str, int]): A dictionary mapping player names to their scores.

    Returns:
    str: A formatted string of the scoreboard.
    """
    formatted = 'Scoreboard:\n'
    for player, score in scores.items():
        formatted += f'{player}: {score}\n'
    return formatted.strip()
