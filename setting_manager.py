from enum import Enum


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


class SettingManager:

    def __init__(self):
        self.settings = {}
        self.change_setting(Setting.NAME, 'DungeonBoop')
        self.change_setting(Setting.VERSION, '0.1')
        self.change_setting(Setting.SCREEN_X, 1200)
        self.change_setting(Setting.SCREEN_Y, 800)
        self.change_setting(Setting.GRIDSIZE_SQUARE, 15)
        self.change_setting(Setting.FPS, 240)
        self.change_setting(Setting.BG_COLOR, 0x444444)
        self.change_setting(Setting.GRID_COLOR, 0x555555)
        self.change_setting(Setting.DUNGEON_COLOR, 0x999999)
        self.change_setting(Setting.BORDER_COLOR, 0x000000)
        self.change_setting(Setting.BORDER_STRENGTH, 2)
        self.change_setting(Setting.GRID_STEP, 3)
        self.change_setting(Setting.GRID_MAX, 100)
        self.change_setting(Setting.GRID_MIN, 9)

    def change_setting(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings[key]

    def set(self, key, value):
        self.change_setting(key, value)

    def get_dungeon_colors(self):
        return [self.settings[Setting.BORDER_COLOR], self.settings[Setting.DUNGEON_COLOR]]


SETTINGS = SettingManager()
