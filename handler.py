import logging

# Configure logger for performance metrics
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance-86')

def validate_frame_data(data: dict) -> bool:
    """Ensures frame input meets schema requirements."""
    required = {'frame_id', 'latency_ms', 'fps'}
    if not all(key in data for key in required):
        return False
    if not isinstance(data['latency_ms'], (int, float)) or data['latency_ms'] < 0:
        return False
    return True

def process_input_stream(stream):
    """Main processing loop with input sanitization."""
    for entry in stream:
        try:
            if not validate_frame_data(entry):
                logger.warning(f"Invalid frame data dropped: {entry.get('frame_id', 'unknown')}")
                continue
            
            # Simulate processing of valid game performance data
            fps = entry['fps']
            latency = entry['latency_ms']
            logger.info(f"Processing frame {entry['frame_id']}: {fps} FPS, {latency}ms")
            
        except Exception as e:
            logger.error(f"Critical processing failure: {e}")

if __name__ == '__main__':
    mock_stream = [
        {'frame_id': 1, 'latency_ms': 16.5, 'fps': 60},
        {'frame_id': 2, 'latency_ms': -5, 'fps': 60},
        {'frame_id': 3, 'latency_ms': 12.0, 'fps': 144}
    ]
    process_input_stream(mock_stream)