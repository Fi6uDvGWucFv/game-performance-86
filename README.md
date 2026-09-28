[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# game-performance-86

`game-performance-86` is a lightweight Python telemetry engine designed to capture, analyze, and visualize real-time frame rates and hardware bottlenecks across x86 PC games. It hooks directly into system graphics pipelines and system metrics to generate actionable performance profiles without introducing render overhead.

## Features

* **Sub-Millisecond Frame Time Tracking:** Measures 1% low and 0.1% low FPS thresholds to identify micro-stutter anomalies during active gameplay.
* **Hardware Bottleneck Detection:** Synchronizes GPU clock speeds, VRAM allocation, and CPU thread saturation with render times.
* **Automated Report Generation:** Exports interactive HTML performance graphs and structured CSV logs at the end of each benchmark session.
* **Minimal System Footprint:** Operates as a background process utilizing under 15MB of RAM and less than 0.5% CPU power.

## Installation

Ensure you have Python 3.9+ installed on your Windows system before proceeding.

```bash
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86
pip install -r requirements.txt
python setup.py install
```

## Basic Usage

Run the telemetry monitor alongside your target game process:

```python
from game_performance import TelemetryMonitor

# Initialize session for the target game process
monitor = TelemetryMonitor(process_name="Cyberpunk2077.exe", interval_ms=100)

# Start collecting metrics
monitor.start()

# ... allow game session to run ...

# Stop logging and save final report
monitor.stop()
monitor.save_report(output_path="session_analysis.html")
```

For quick CLI benchmarking without writing code:

```bash
python -m game_performance --process EldenRing.exe --duration 300 --output report.csv
```

## License

Distributed under the MIT License. See `LICENSE` for more information.