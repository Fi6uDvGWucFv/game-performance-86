import json
from typing import Dict, List, Any, Optional

def sanitize_game_metrics(data: Dict[str, Any]) -> Dict[str, Any]:
    """Cleans raw telemetry data for processing."""
    required_fields = {'session_id', 'fps', 'ping'}
    
    # Filter to only known valid metrics
    sanitized = {
        k: v for k, v in data.items() 
        if k in required_fields and v is not None
    }
    
    # Enforce type constraints for performance analysis
    if 'fps' in sanitized:
        sanitized['fps'] = float(sanitized['fps'])
    if 'ping' in sanitized:
        sanitized['ping'] = int(sanitized['ping'])
        
    return sanitized

def batch_process_metrics(metrics: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Processes list of metrics and returns valid entries."""
    return [sanitize_game_metrics(m) for m in metrics if all(k in m for k in ['session_id'])]

def export_metrics_to_json(metrics: List[Dict[str, Any]], filepath: str) -> bool:
    """Persists processed metrics to local storage."""
    try:
        with open(filepath, 'w') as f:
            json.dump(metrics, f, indent=4)
        return True
    except (IOError, TypeError):
        return False