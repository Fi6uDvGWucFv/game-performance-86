import time

class Game:
    def __init__(self, name, fps_limit=60):
        self.name = name
        self.fps_limit = fps_limit
        self.last_frame_time = time.time()
        self.delta_time = 0

    def start(self):
        print(f'Starting game: {self.name}')
        self.main_loop()

    def main_loop(self):
        while True:
            self.update()
            self.render()
            self.sleep()

    def update(self):
        print('Updating game state...')

    def render(self):
        print('Rendering frame...')

    def sleep(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_frame_time
        frame_time = 1.0 / self.fps_limit
        if self.delta_time < frame_time:
            time.sleep(frame_time - self.delta_time)
        self.last_frame_time = time.time()