import numpy as np

def calculate_fps(frame_times):
    '''Calculate frames per second from a list of frame times.'''
    if not frame_times:
        return 0
    average_time = sum(frame_times) / len(frame_times)
    fps = 1 / average_time if average_time > 0 else 0
    return fps


def optimize_sprite_rendering(sprites):
    '''Optimize sprite rendering using spatial partitioning.'''
    grid = {}  # Dictionary to hold sprites by grid cell
    for sprite in sprites:
        cell_key = (int(sprite.x // 64), int(sprite.y // 64))  # Assuming grid size of 64x64
        if cell_key not in grid:
            grid[cell_key] = []
        grid[cell_key].append(sprite)
    return grid


def batch_render_sprites(sprites):
    '''Batch render sprites for better performance.'''
    grid = optimize_sprite_rendering(sprites)
    for cell in grid.values():
        # Assuming a render function exists that takes a list of sprites
        render(cell)  # Render each batch of sprites in the same cell


def smooth_motion(sprite, target_position, delta_time):
    '''Smoothly interpolate a sprite's position towards a target.'''
    speed = sprite.speed * delta_time
    direction = np.array(target_position) - np.array([sprite.x, sprite.y])
    distance = np.linalg.norm(direction)
    if distance > speed:
        direction = direction / distance  # Normalize direction
        sprite.x += direction[0] * speed
        sprite.y += direction[1] * speed
    else:
        sprite.x = target_position[0]
        sprite.y = target_position[1]

