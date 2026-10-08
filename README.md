# game-performance-86

A high-performance Python toolkit designed to analyze, monitor, and optimize hardware telemetry during intensive gaming sessions. This library bridges the gap between raw system metrics and actionable performance insights for developers and enthusiasts alike.

## Features

*   **Real-time Telemetry:** Stream frame-time consistency, GPU temperature, and VRAM utilization with sub-millisecond precision.
*   **Bottleneck Detection:** Automated heuristic analysis to identify CPU-bound versus GPU-bound frames.
*   **CSV Log Export:** Generate formatted performance reports compatible with Excel and Tableau for deep-dive analysis.
*   **Low-Overhead Profiling:** Optimized background threading ensures that the monitoring process consumes less than 0.5% of total system CPU load.

## Installation

Ensure you have Python 3.8+ installed on your system. Install the package via pip:

```bash
pip install game-performance-86
```

For hardware monitoring access on Windows, you may need to run your terminal as an Administrator.

## Basic Usage

Import the `PerformanceMonitor` class to start tracking your system statistics immediately.

```python
from gp86 import PerformanceMonitor

# Initialize the monitor
monitor = PerformanceMonitor(interval=0.1)

# Start tracking in the background
monitor.start()

try:
    while True:
        # Fetch current frame stats
        stats = monitor.get_latest()
        print(f"Current FPS: {stats['fps']} | GPU Load: {stats['gpu_load']}%")
except KeyboardInterrupt:
    monitor.stop()
    monitor.save_report("session_log.csv")
```

## Requirements
*   **OS:** Windows 10/11 (DirectX support required)
*   **Dependencies:** `psutil`, `pywin32`

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.