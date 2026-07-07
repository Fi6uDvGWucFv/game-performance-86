from typing import List, Dict


def calculate_frame_rate(frames: int, time_seconds: float) -> float:
    """
    Calculate the frame rate based on the number of frames and the elapsed time.

    Args:
        frames (int): The number of frames rendered.
        time_seconds (float): The time in seconds over which the frames were rendered.

    Returns:
        float: The calculated frame rate.
    """
    if time_seconds <= 0:
        raise ValueError('Time must be greater than zero.')
    return frames / time_seconds


def average_fps(fps_values: List[float]) -> float:
    """
    Calculate the average frames per second (FPS).

    Args:
        fps_values (List[float]): A list of FPS values.

    Returns:
        float: The average FPS.
    """
    if not fps_values:
        raise ValueError('FPS values list cannot be empty.')
    return sum(fps_values) / len(fps_values)


def prepare_game_stats(frames: int, elapsed_time: float, fps_values: List[float]) -> Dict[str, float]:
    """
    Prepare a summary of game statistics including frame rate and average FPS.

    Args:
        frames (int): The number of frames rendered.
        elapsed_time (float): Elapsed time in seconds.
        fps_values (List[float]): A list of FPS values.

    Returns:
        Dict[str, float]: A dictionary containing 'frame_rate' and 'average_fps'.
    """
    frame_rate = calculate_frame_rate(frames, elapsed_time)
    average_fps_value = average_fps(fps_values)
    return {'frame_rate': frame_rate, 'average_fps': average_fps_value}