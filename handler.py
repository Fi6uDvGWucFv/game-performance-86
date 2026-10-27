import json
from typing import Dict, List, Optional

def process_frame_data(raw_data: str) -> Dict:
    """
    Parses raw telemetry strings from game engines and validates
    essential performance metrics like fps and latency.
    """
    try:
        data = json.loads(raw_data)
        
        # Ensure required metrics exist to prevent downstream errors
        required_fields = ['fps', 'latency_ms', 'frame_time']
        if not all(field in data for field in required_fields):
            return {'status': 'error', 'message': 'missing metrics'}
            
        # Normalize values to ensure consistent data types for analytics
        return {
            'status': 'success',
            'fps': int(data.get('fps', 0)),
            'latency': float(data.get('latency_ms', 0.0)),
            'frame_time': float(data.get('frame_time', 0.0))
        }
    except (json.JSONDecodeError, ValueError, TypeError):
        return {'status': 'error', 'message': 'invalid payload'}

def aggregate_metrics(metrics: List[Dict]) -> Dict:
    """
    Calculates average performance metrics across a collected list
    of game frames.
    """
    if not metrics:
        return {'avg_fps': 0, 'avg_latency': 0}
        
    count = len(metrics)
    avg_fps = sum(m.get('fps', 0) for m in metrics) / count
    avg_latency = sum(m.get('latency', 0) for m in metrics) / count
    
    return {
        'avg_fps': round(avg_fps, 2),
        'avg_latency': round(avg_latency, 2)
    }