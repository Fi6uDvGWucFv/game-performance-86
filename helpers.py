def calculate_fps(start_time, end_time, frame_count):
    """
    Calculate frames per second (FPS) based on time and frame count.
    """
    elapsed_time = end_time - start_time
    if elapsed_time > 0:
        return frame_count / elapsed_time
    return 0


def load_texture(texture_path):
    """
    Load a texture from the given file path.
    """
    try:
        from PIL import Image
        texture = Image.open(texture_path)
        return texture
    except Exception as e:
        print(f'Error loading texture: {e}')
        return None


def check_collision(rect_a, rect_b):
    """
    Check if two rectangles collide.
    """
    return (rect_a['x'] < rect_b['x'] + rect_b['width'] and 
            rect_a['x'] + rect_a['width'] > rect_b['x'] and 
            rect_a['y'] < rect_b['y'] + rect_b['height'] and 
            rect_a['y'] + rect_a['height'] > rect_b['y'])


def interpolate(start, end, factor):
    """
    Interpolate between start and end values.
    """
    return start + (end - start) * factor


if __name__ == '__main__':
    # Example usage of the helper functions
    fps = calculate_fps(0.0, 1.0, 60)
    print(f'Calculated FPS: {fps}')