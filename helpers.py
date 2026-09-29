from typing import List, Dict, Union, Optional

def calculate_frame_time_stats(frame_times: List[float]) -> Dict[str, float]:
    """Calculates average and peak frame times for performance monitoring."""
    if not frame_times:
        return {"avg": 0.0, "peak": 0.0}
    
    avg_time: float = sum(frame_times) / len(frame_times)
    peak_time: float = max(frame_times)
    return {"avg": avg_time, "peak": peak_time}

def format_memory_usage(bytes_count: int) -> str:
    """Converts raw byte count into a human-readable megabyte string."""
    mb_value: float = bytes_count / (1024 * 1024)
    return f"{mb_value:.2f} MB"

def get_gpu_load_status(load_percentage: float) -> str:
    """Categorizes GPU load intensity for diagnostic output."""
    if load_percentage > 90.0:
        return "critical"
    elif load_percentage > 70.0:
        return "high"
    return "stable"

def filter_active_tasks(tasks: List[Dict[str, Union[str, bool]]]) -> List[Dict[str, Union[str, bool]]]:
    """Filters list of game tasks to return only those currently running."""
    return [task for task in tasks if task.get("is_active", False)]