from pygame import Color

from src.Uilib.view import View


class SelectListView(View):

    def __init__(self, surface, entries, font, color, padding=5, name='SelectListView'):
        super().__init__(surface)
        self.entries = entries
        self.max = len(entries)
        self.selected_entry = 0
        self.font = font
        self.color = color
        self.font_height = self.font.size('Pg')[1]
        self.padding = padding
        self.name = name

    def render(self, x, mid_y):
        start = max(self.selected_entry - 2, 0)
        end = min(self.selected_entry + 3, self.max)
        delta = start - self.selected_entry + 2
        y = mid_y - (self.font_height + self.padding) * (2 - delta)
        alphas = [50, 100, 255, 100, 50]
        for i, entry in enumerate(self.entries[start: end]):
            color = Color(self.color)
            color.a = alphas[i + delta]
            color = color.premul_alpha()
            text = ("> " if entry == self.entries[self.selected_entry] else "") + entry
            text_surface = self.font.render(text, False, color)
            self.surface.blit(text_surface, (x, y - self.font_height))
            y += self.font_height + self.padding

    def next(self):
        self.selected_entry = min(self.max-1, self.selected_entry + 1)

    def previous(self):
        self.selected_entry = max(0, self.selected_entry - 1)

    def get_selected(self):
        return self.entries[self.selected_entry]
