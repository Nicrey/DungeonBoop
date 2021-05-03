from enum import Enum

import pygame


class Actions(Enum):
    EXIT = 0
    MOUSE_LEFT_EVENT = 1
    MOUSE_RIGHT_EVENT = 2
    SCREEN_RESIZE = 3


class Action:
    def __init__(self, action: Actions, values: {}):
        self.name = action
        self.values = values


class KeybindManager():
    def __init__(self):
        self.keybinds = {}
        self.set_keybind(Actions.MOUSE_LEFT_EVENT, [pygame.MOUSEBUTTONUP])

    def set_keybind(self, action, keybind):
        self.keybinds[keybind] = action

