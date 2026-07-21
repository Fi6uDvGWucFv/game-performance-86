import time
import random

class Game:
    def __init__(self, name):
        self.name = name
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        start_time = time.perf_counter()
        for entity in self.entities:
            entity.update()
        end_time = time.perf_counter()
        self.optimize_performance(end_time - start_time)

    def optimize_performance(self, duration):
        if duration > 0.016:  # Roughly 60 FPS
            print(f'Performance optimization needed. Frame duration: {duration:.3f}s')
            self.entities = self.entities[:100]  # Keep only the first 100 entities

class Entity:
    def __init__(self, id):
        self.id = id
        self.position = (random.randint(0, 100), random.randint(0, 100))

    def update(self):
        self.position = (self.position[0] + 1, self.position[1] + 1)  # Move entity

# Example usage
if __name__ == '__main__':
    game = Game('Sample Game')
    for i in range(150):  # Adding more entities than needed
        game.add_entity(Entity(i))
    while True:
        game.update()