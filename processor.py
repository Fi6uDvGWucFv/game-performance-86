import json
from typing import Dict, Any, List, Optional

def normalize_game_metrics(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes raw game telemetry metrics for analysis."""
    processed = {
        "session_id": str(data.get("sid", "unknown")),
        "fps_avg": float(data.get("fps", 0.0)),
        "frame_time_ms": float(data.get("ft", 0.0)),
        "dropped_frames": int(data.get("df", 0)),
        "timestamp": data.get("ts", 0)
    }
    
    # Calculate performance health score
    processed["health_index"] = round(processed["fps_avg"] / (processed["frame_time_ms"] + 1), 2)
    
    return processed

def batch_process_metrics(payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Processes list of telemetry objects into clean structures."""
    results = []
    for entry in payloads:
        try:
            results.append(normalize_game_metrics(entry))
        except (ValueError, TypeError):
            continue
    return results

def format_for_db(metrics: Dict[str, Any]) -> str:
    """Serializes processed metrics for database storage."""
    return json.dumps(metrics)