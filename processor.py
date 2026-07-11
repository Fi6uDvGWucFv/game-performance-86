import time

class GameProcessor:
    def __init__(self, game_id):
        self.game_id = game_id
        self.start_time = None
        self.end_time = None

    def start_processing(self):
        self.start_time = time.time()
        print(f"Processing started for game {self.game_id}")

    def end_processing(self):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"Processing ended for game {self.game_id} in {duration:.2f} seconds")
        return duration

    def reset(self):
        self.start_time = None
        self.end_time = None
        print(f"Processor for game {self.game_id} has been reset")

if __name__ == '__main__':
    processor = GameProcessor(86)
    processor.start_processing()
    time.sleep(2)  # Simulate game processing time
    processor.end_processing()