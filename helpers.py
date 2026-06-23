def optimize_performance(data):
    # Reduce unnecessary calculations
    optimized_data = []
    seen = set()
    for item in data:
        if item not in seen:
            seen.add(item)
            optimized_data.append(item)
    return optimized_data


def calculate_average(frames):
    # Use more efficient calculation for average
    return sum(frames) / len(frames) if frames else 0


def frame_rate_statistics(frames):
    # Compute min, max and average frame rates
    if not frames:
        return {'min': 0, 'max': 0, 'average': 0}
    min_frame = min(frames)
    max_frame = max(frames)
    average_frame = calculate_average(frames)
    return {'min': min_frame, 'max': max_frame, 'average': average_frame}


def log_performance(frames):
    stats = frame_rate_statistics(frames)
    print(f"Performance Stats - Min: {stats['min']}, Max: {stats['max']}, Average: {stats['average']}")

# Example Usage:
# frames = [60, 55, 60, 70, 60, 55, 80]
# log_performance(frames)