![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# game-performance-86

`game-performance-86` is a lightweight Python telemetry engine designed to capture, log, and analyze real-time gaming metrics on x86 architectures. It provides low-overhead frame time tracking, hardware utilization monitoring, and automated benchmark report generation without impacting rendering performance.

## Features

- **Sub-Millisecond Frame-Time Tracking**: Hooks into Direct3D and Vulkan APIs to record precise frame intervals and calculate accurate 1% and 0.1% low FPS metrics.
- **Hardware Telemetry Logging**: Tracks real-time CPU core loads, GPU temperatures, VRAM consumption, and system memory limits with minimal overhead.
- **Automated Report Generation**: Exports clean CSV logs and compiles interactive HTML performance summaries directly after a game exits.
- **Thermal Throttling Detection**: Triggers immediate alerts when clock speeds drop due to thermal limits during gameplay.

## Installation

Ensure you have Python 3.9+ installed on your system.

```bash
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86
pip install -r requirements.txt
pip install .
```

## Basic Usage

Run a telemetry session by pointing `game-performance-86` at an active executable:

```python
from game_performance import Profiler, ReportGenerator

# Initialize telemetry target
profiler