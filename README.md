# game-performance-86

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

game-performance-86 is a Python library for profiling and optimizing performance in real-time games. It helps developers identify frame time inconsistencies, memory spikes, and subsystem bottlenecks without adding significant overhead to the game loop.

## Features
- Microsecond-accurate frame timing with percentile analysis (p50, p99)
- Memory allocation tracking for textures, audio buffers, and object pools
- Automatic detection of hitches and long frames with stack context
- Native integration hooks for Pygame and custom rendering pipelines

## Installation

```bash
pip install game-performance-86
```

For development installation:

```bash
git clone https://github.com/Developer/game-performance-86.git
cd game-performance-86
pip install -e .
```

## Usage

```python
from game_performance_86 import GameProfiler

profiler = GameProfiler()

running = True
while running:
    with profiler.profile_frame():
        process_input()
        update_world()
        render_scene()

profiler.save_report("perf_report.json")
```

The profiler can run in both development and lightly instrumented release builds.