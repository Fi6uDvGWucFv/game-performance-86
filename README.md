# game-performance-86

`game-performance-86` is a lightweight Python toolkit designed to monitor and optimize system resources during gaming sessions. It provides real-time telemetry to help identify bottlenecks and minimize latency in resource-heavy environments.

## Features

*   **Real-time Metrics:** Tracks CPU/GPU temperatures, usage percentages, and memory allocation with sub-second polling rates.
*   **Background Throttling:** Automatically suspends non-essential background processes when a defined game executable is detected.
*   **Frame-Time Logging:** Captures per-frame performance data to a CSV file for post-session analysis and stability testing.
*   **Low-Overhead CLI:** Optimized for minimal resource footprint, ensuring the monitor itself doesn't impact your frame rate.

## Installation

Ensure you have Python 3.8+ installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86
pip install -r requirements.txt
```

## Usage

To start monitoring a specific process (e.g., `eldenring.exe`), run the tool with administrative privileges:

```bash
# Monitor a specific process by name
sudo python monitor.py --process eldenring.exe --log performance_log.csv
```

The script will output a live dashboard to your terminal and begin writing performance metrics to `performance_log.csv`. To stop the monitoring session, press `Ctrl+C`.

## Configuration

You can customize the polling interval and target thresholds by editing the `config.yaml` file located in the root directory. Adjust the `throttle_threshold` settings to suit your system's hardware limitations.

---
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)