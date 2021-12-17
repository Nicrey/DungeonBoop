import pygame


class CanvasView:

    def __init__(self,surface,canvas, pixels=None):
        self.canvas = canvas
        self.name = 'CANVAS_VIEW'
        self.surface = surface
        if pixels is not None:
            self.canvas.dungeon_pixels = pixels
        else:
            self.canvas.reset()

    def render(self):
        changed_x, changed_y = self.canvas.get_changes()
        if not changed_x:
            return
        min_x = changed_x[0]
        max_x = changed_x[-1]
        min_y = changed_y[0]
        max_y = changed_y[-1]
        pixels = pygame.surfarray.pixels2d(self.surface)
        pixels[:] = self.canvas.get_pixels()
        update_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        pygame.display.update(update_rect)
