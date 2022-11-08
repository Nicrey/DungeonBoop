from enum import Enum

import pygame

class Setting(Enum):
    NAME = 1
    VERSION = 2
    SCREEN_X = 3
    SCREEN_Y = 4
    GRIDSIZE_SQUARE = 5
    FPS = 6
    BG_COLOR = 7
    GRID_COLOR = 8
    DUNGEON_COLOR = 9
    BORDER_COLOR = 10
    BORDER_STRENGTH = 11
    GRID_STEP = 12
    GRID_MAX = 13
    GRID_MIN = 14
    FONT_PATH = 15
    FONT_SIZE = 16
    FONT_COLOR = 17
    PROJECT_BACK_COLOR = 18


class SettingManager:

    def __init__(self):
        pygame.font.init()
        self.settings = {}
        self.change_setting(Setting.NAME, 'DungeonBoop')
        self.change_setting(Setting.VERSION, '0.1')
        self.change_setting(Setting.SCREEN_X, 1024)
        self.change_setting(Setting.SCREEN_Y, 1024)
        self.change_setting(Setting.GRIDSIZE_SQUARE, 16)
        self.change_setting(Setting.FPS, 240)
        self.change_setting(Setting.BG_COLOR, 0x444444)
        self.change_setting(Setting.GRID_COLOR, 0x555555)
        self.change_setting(Setting.DUNGEON_COLOR, 0x999999)

        self.change_setting(Setting.BORDER_COLOR, 0x000000)
        self.change_setting(Setting.BORDER_STRENGTH, 2)
        self.change_setting(Setting.GRID_STEP, 2)
        self.change_setting(Setting.GRID_MAX, 128)
        self.change_setting(Setting.GRID_MIN, 8)
        
        from src.Util.file_manager import resource_path
        self.change_setting(Setting.FONT_PATH, resource_path('resources/FreeMono.otf'))
        self.change_setting(Setting.FONT_SIZE, 45)
        self.change_setting(Setting.FONT_COLOR, (100, 100, 255))
        self.change_setting(Setting.PROJECT_BACK_COLOR, (0, 0, 0))

    def change_setting(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings[key]

    def set(self, key, value):
        self.change_setting(key, value)

    def get_dungeon_colors(self):
        return [self.settings[Setting.BORDER_COLOR], self.settings[Setting.DUNGEON_COLOR]]

    def get_font(self):
        print(self.settings[Setting.FONT_PATH])
        return pygame.font.Font(self.settings[Setting.FONT_PATH], self.settings[Setting.FONT_SIZE])


SETTINGS = SettingManager()
