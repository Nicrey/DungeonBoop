import numpy

from setting_manager import Setting, SETTINGS


class Canvas:

    def __init__(self, size_x, size_y):
        self.dungeon_pixels = numpy.zeros((size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        grid_size = SETTINGS.get(Setting.GRIDSIZE_SQUARE)
        for x in range(self.size_x):
            for y in range(self.size_y):
                if x % grid_size == 0 and y % grid_size == 0:
                    self.dungeon_pixels[x, y] = SETTINGS.get(Setting.GRID_COLOR)
                else:
                    self.dungeon_pixels[x, y] = SETTINGS.get(Setting.BG_COLOR)

    def get_pixels(self):
        return self.dungeon_pixels

    def pixel_clicked(self, pos, remove):
        grid_size = SETTINGS.get(Setting.GRIDSIZE_SQUARE)
        color = SETTINGS.get(Setting.BG_COLOR) if remove else SETTINGS.get(Setting.DUNGEON_COLOR)
        x_delta = pos[0] % grid_size
        y_delta = pos[1] % grid_size
        for x in range(pos[0] - x_delta, pos[0] - x_delta + grid_size):
            for y in range(pos[1] - y_delta, pos[1] - y_delta + grid_size):
                self.dungeon_pixels[x, y] = color
