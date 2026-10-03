import logging

# Configure logger for performance metrics
logger = logging.getLogger('game-performance-86')

def validate_input(data):
    """Ensures incoming game telemetry is within valid ranges."""
    if not isinstance(data, dict):
        return False
    if 'frame_time' not in data or not (0 < data['frame_time'] < 1000):
        return False
    if 'gpu_temp' not in data or not (0 < data['gpu_temp'] < 120):
        return False
    return True

def process_telemetry(stream):
    """Main loop for processing real-time game performance data."""
    for packet in stream:
        try:
            if not validate_input(packet):
                logger.warning(f"Invalid packet dropped: {packet}")
                continue
            
            # Simulate core performance logic
            fps = 1000 / packet['frame_time']
            logger.info(f"Processed performance: {fps:.2f} FPS")
            
        except Exception as e:
            logger.error(f"Processing error: {str(e)}")

if __name__ == '__main__':
    # Example usage for performance testing
    test_stream = [
        {'frame_time': 16.6, 'gpu_temp': 65},
        {'frame_time': -5, 'gpu_temp': 50},
        {'frame_time': 33.3, 'gpu_temp': 70}
    ]
    process_telemetry(test_stream)