import pygame

from src.Uilib.input_text_view import InputTextView
from src.Uilib.select_list_view import SelectListView
from src.Util.file_manager import FILES
from src.Util.keybind_manager import KEYBINDS, Actions
from src.Util.setting_manager import Setting, SETTINGS


class ProjectOverview(SelectListView):

    def __init__(self, surface, projects):
        self.projects = projects
        self.names = [p.name for p in projects]
        super().__init__(surface, self.names, SETTINGS.get_font(), SETTINGS.get(Setting.FONT_COLOR))
        self.font = SETTINGS.get_font()
        self.surface = surface
        self.name = 'PROJECT_OVERVIEW'

    def render(self):
        self.surface.fill(SETTINGS.get(Setting.PROJECT_BACK_COLOR))
        if not self.names:
            text = f"Press {KEYBINDS.reverse_lookup[Actions.NEW_PROJECT]} to CREATE a new Project."
            textsurface = self.font.render(text, False, (255, 0, 0))
            self.surface.blit(textsurface, (0, 0))
        else:
            width, height = self.surface.get_size()
            super().render(width/10, height/2)

    def get_selected(self):
        name = super().get_selected()
        return [p for p in self.projects if p.name == name][0]