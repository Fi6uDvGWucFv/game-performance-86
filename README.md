# game-performance-86

A high-performance Python toolkit designed to analyze and optimize system resource allocation for competitive gaming. This utility bridges the gap between hardware telemetry and game engine behavior to minimize input lag and frame stutter.

## Features

*   **Real-time Process Priority Management:** Automatically elevates your active game process and assigns CPU affinity to prevent background task interference.
*   **Thermal Throttling Monitor:** Tracks GPU and CPU junction temperatures, triggering proactive fan profile adjustments via external hardware drivers.
*   **Dynamic Background Cleanup:** Periodically purges system memory caches and suspends non-essential telemetry services during active gaming sessions.
*   **Frame-Time Log Analyzer:** Parses standard CSV export files from engine overlays (like PresentMon) to calculate 0.1% and 1% low frame rates.

## Installation

Ensure you have Python 3.9+ installed. It is recommended to run this tool in a virtual environment.

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86

# Install required dependencies
pip install -r requirements.txt
```

## Usage

To start the optimization monitor in background mode, target your game executable by name:

```bash
# Run with administrative privileges for process management
sudo python main.py --process "elden_ring.exe" --priority high
```

To run a diagnostic on an existing frame-time log:

```bash
python analyzer.py --input logs/session_01.csv --report summary
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.