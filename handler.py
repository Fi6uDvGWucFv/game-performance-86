import json
from typing import List, Dict, Any

def format_game_telemetry(data: List[Dict[str, Any]]) -> str:
    """Processes raw performance logs into structured JSON."""
    processed = []
    for entry in data:
        # Ensure basic metrics exist to avoid corrupt data entries
        if 'fps' in entry and 'frame_time' in entry:
            processed.append({
                'timestamp': entry.get('ts', 0),
                'fps': float(entry['fps']),
                'frame_ms': round(float(entry['frame_time']), 2),
                'gpu_load': entry.get('gpu', 0),
                'status': 'stable' if entry['fps'] > 30 else 'lagging'
            })
    
    return json.dumps({'count': len(processed), 'metrics': processed})

def calculate_average_latency(data: List[Dict[str, Any]]) -> float:
    """Computes mean frame time across the provided window."""
    latencies = [d.get('frame_time', 0) for d in data if isinstance(d.get('frame_time'), (int, float))]
    if not latencies:
        return 0.0
    return sum(latencies) / len(latencies)