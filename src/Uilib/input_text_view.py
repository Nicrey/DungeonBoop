import re

import pygame

from src.Uilib.view import View
from src.Util.setting_manager import SETTINGS, Setting


class InputTextView(View):

    def __init__(self, surface, font, color, text="", allowed_regex=None, name='InputTextView'):
        super().__init__(surface)
        self.text = text
        self.color = color
        self.allowed_regex = allowed_regex
        self.font = font
        self.name = name
        self.font_height = font.size('Pg')[1]

    def render(self, x, y):
        self.surface.fill(SETTINGS.get(Setting.PROJECT_BACK_COLOR))
        text = ">" + self.text
        text_surface = self.font.render(text, False, self.color)
        self.surface.blit(text_surface, (x, y - self.font_height))

    def add_char(self, char):
        if self.allowed_regex:
            if not re.match(self.allowed_regex, char):
                return
        self.text += char

    def remove(self):
        self.text = self.text[-1]

    def back(self):
        self.remove()

    def clear(self):
        self.text = ''

    def get_text(self):
        return self.text
