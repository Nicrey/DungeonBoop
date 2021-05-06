import numpy

from setting_manager import Setting, SETTINGS
from sortedcontainers import SortedList


class Canvas:

    def __init__(self, size_x, size_y):
        self.changed_x = SortedList()
        self.changed_y = SortedList()
        self.dungeon_pixels = numpy.zeros((size_x, size_y))
        self.grid = numpy.zeros((size_x, size_y))
        self.bg_neighbors = numpy.zeros((size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.draw_grid(100)
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.paint_pixel(x, y, SETTINGS.get(Setting.BG_COLOR))

    def get_changes(self):
        return self.changed_x, self.changed_y

    def get_pixels(self):
        self.changed_x = SortedList()
        self.changed_y = SortedList()
        ret = self.dungeon_pixels - self.grid
        return ret

    def increase_grid(self):
        self.change_grid(increase=True)

    def decrease_grid(self):
        self.change_grid(increase=False)

    def change_grid(self, increase: bool):
        old_size = SETTINGS.get(Setting.GRIDSIZE_SQUARE)
        step = SETTINGS.get(Setting.GRID_STEP)
        new = old_size + (step if increase else -step)
        bounded = min(max(new, SETTINGS.get(Setting.GRID_MIN)), SETTINGS.get(Setting.GRID_MAX))
        SETTINGS.set(Setting.GRIDSIZE_SQUARE, bounded)
        self.draw_grid(old_size)

    def pixel_clicked(self, pos, remove):
        grid_size = SETTINGS.get(Setting.GRIDSIZE_SQUARE)
        border_size = SETTINGS.get(Setting.BORDER_STRENGTH) * 2
        color = SETTINGS.get(Setting.BG_COLOR) if remove else SETTINGS.get(Setting.DUNGEON_COLOR)
        x_delta = pos[0] % grid_size
        y_delta = pos[1] % grid_size
        x_start, x_end = pos[0] - x_delta, min(pos[0] - x_delta + grid_size, self.size_x)
        y_start, y_end = pos[1] - y_delta, min(pos[1] - y_delta + grid_size, self.size_y)
        self.changed_x.add(x_start - border_size)
        self.changed_x.add(x_end + border_size)
        self.changed_y.add(y_start - border_size)
        self.changed_y.add(y_end + border_size)
        # Set Inner Square where we dont have to think about borders
        self.dungeon_pixels[x_start + border_size:x_end - border_size, y_start + border_size:y_end - border_size] = color
        self.bg_neighbors[x_start + border_size:x_end - border_size, y_start + border_size:y_end - border_size] = 0

        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if x_start + border_size < x < x_end-border_size and y_start + border_size < y < y_end -border_size:
                    continue
                # When color switches
                if self.dungeon_pixels[x, y] not in SETTINGS.get_dungeon_colors() and not remove:
                    self.check_neighbors_for_add(x, y)
                if self.dungeon_pixels[x, y] in SETTINGS.get_dungeon_colors() and remove:
                    self.check_neighbors_for_remove(x, y)
                if self.dungeon_pixels[x, y] != SETTINGS.get(Setting.BORDER_COLOR) or remove:
                    self.paint_pixel(x, y, color)

    def check_neighbors_for_remove(self, x, y):
        self.bg_neighbors[x, y] = 0
        x_range, y_range = self.get_neighbor_ranges(x, y)
        for dx in x_range:
            if dx == x:
                continue
            self.check_neighbor_pixel_for_remove(dx, y)
        for dy in y_range:
            if dy == y:
                continue
            self.check_neighbor_pixel_for_remove(x, dy)

    def check_neighbors_for_add(self, main_x, main_y):
        self.bg_neighbors[main_x, main_y] = 0
        x_range, y_range = self.get_neighbor_ranges(main_x, main_y)
        for x in x_range:
            if x == main_x:
                continue
            self.check_neighbor_pixel_for_add(x, main_y)
            self.check_neighbor_for_bg(x, main_y, main_x, main_y)
        for y in y_range:
            if y == main_y:
                continue
            self.check_neighbor_pixel_for_add(main_x, y)
            self.check_neighbor_for_bg(main_x, y, main_x, main_y)

        if self.bg_neighbors[main_x, main_y] > 0:
            self.paint_pixel(main_x, main_y, SETTINGS.get(Setting.BORDER_COLOR))

    def paint_pixel(self, x, y, color):
        self.dungeon_pixels[x, y] = color

    def check_neighbor_pixel_for_add(self, x, y):
        if self.dungeon_pixels[x, y] in SETTINGS.get_dungeon_colors():
            self.bg_neighbors[x, y] = max(self.bg_neighbors[x, y] - 1, 0)
            if self.bg_neighbors[x, y] == 0 and self.dungeon_pixels[x, y] == SETTINGS.get(Setting.BORDER_COLOR):
                self.paint_pixel(x, y, SETTINGS.get(Setting.DUNGEON_COLOR))

    def check_neighbor_pixel_for_remove(self, x, y):
        if self.dungeon_pixels[x, y] in SETTINGS.get_dungeon_colors():
            self.bg_neighbors[x, y] += 1
            self.paint_pixel(x, y, SETTINGS.get(Setting.BORDER_COLOR))

    def check_neighbor_for_bg(self, x, y, main_x, main_y):
        if self.dungeon_pixels[x, y] == SETTINGS.get(Setting.BG_COLOR):
            self.bg_neighbors[main_x, main_y] += 1

    def get_neighbor_ranges(self, x, y):
        border_size = SETTINGS.get(Setting.BORDER_STRENGTH)
        min_x = max(0, x - border_size)
        max_x = min(self.size_x - 1, x + border_size)
        min_y = max(0, y - border_size)
        max_y = min(self.size_y - 1, y + border_size)
        return range(min_x, max_x + 1), range(min_y, max_y + 1)

    def draw_grid(self, old_size):
        self.grid[::old_size, ::old_size] = 0
        grid_size = SETTINGS.get(Setting.GRIDSIZE_SQUARE)
        self.grid[::grid_size, ::grid_size] = SETTINGS.get(Setting.GRID_COLOR)
        self.changed_x.add(0)
        self.changed_x.add(self.size_x)
        self.changed_y.add(0)
        self.changed_y.add(self.size_y)
