import pygame
import numpy


def draw(surface, canvas):
    pixels = pygame.surfarray.pixels2d(surface)
    changed_x, changed_y = canvas.get_changes()
    if not changed_x:
        return
    min_x = changed_x[0]
    max_x = changed_x[-1]
    min_y = changed_y[0]
    max_y = changed_y[-1]
    pixels[:] = canvas.get_pixels()
    update_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    pygame.display.update(update_rect)
