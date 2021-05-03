import pygame
import numpy


def draw(surface, canvas):
    pixels = pygame.surfarray.pixels2d(surface)
    pixels[:] = canvas.get_pixels()
    pygame.display.update()