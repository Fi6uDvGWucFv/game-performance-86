from typing import List, Dict


def calculate_average(scores: List[int]) -> float:
    """
    Calculate the average of a list of scores.

    Args:
        scores (List[int]): A list of integer scores.

    Returns:
        float: The average of the scores, or 0.0 if the list is empty.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def format_score(score: int) -> str:
    """
    Format the score as a string with a suffix.

    Args:
        score (int): The score to format.

    Returns:
        str: The formatted score string.
    """
    return f'Score: {score}'


def filter_high_scores(scores: List[int], threshold: int) -> List[int]:
    """
    Filter the list of scores, keeping only those above the threshold.

    Args:
        scores (List[int]): A list of integer scores.
        threshold (int): The score threshold.

    Returns:
        List[int]: A list of scores above the threshold.
    """
    return [score for score in scores if score > threshold]


# Example usage
if __name__ == '__main__':
    sample_scores = [88, 92, 79, 95, 84]
    print('Average Score:', calculate_average(sample_scores))
    print(format_score(92))
    print('High Scores:', filter_high_scores(sample_scores, 90))