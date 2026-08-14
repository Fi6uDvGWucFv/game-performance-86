# Game Performance 86

Game Performance 86 is a Python-based tool designed to monitor and optimize the performance of your gaming sessions. It provides real-time analytics on various metrics, allowing gamers to enhance their gaming experience by identifying performance bottlenecks.

## Features
- **Real-Time FPS Monitoring**: Get live updates on frames per second (FPS) to ensure smooth gameplay.
- **Resource Usage Tracking**: Analyze CPU, GPU, and memory usage to identify any resource constraints during gaming.
- **Customizable Alerts**: Set thresholds for performance metrics and receive notifications when they are exceeded.
- **Detailed Reports**: Generate comprehensive reports to review performance metrics over time, helping you make informed decisions about game settings.

## Installation

To install Game Performance 86, ensure you have Python 3.6 or greater installed on your system. Then, execute the following commands in your terminal:

```bash
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86
pip install -r requirements.txt
```

## Basic Usage

After installation, you can start monitoring your gaming performance with just a simple command. Run the following command in your terminal:

```bash
python performance_monitor.py
```

Once running, the tool will display real-time FPS, CPU, GPU, and memory usage, along with any alerts if thresholds are exceeded. For detailed logging, use:

```bash
python performance_monitor.py --log
```

This will create a performance_report.txt file in the current directory with a complete overview of your gaming session.

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.