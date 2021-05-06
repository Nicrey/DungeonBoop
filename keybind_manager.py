from enum import Enum

import pygame


class Actions(Enum):
    EXIT = 0
    ADD_TILE = 1
    REMOVE_TILE = 2
    SCREEN_RESIZE = 3
    INCREASE_GRID_STEP = 4
    DECREASE_GRID_STEP = 5
    RESET = 6
    SAVE = 7


class Action:
    def __init__(self, action: Actions, values: {}):
        self.name = action
        self.values = values


class KeybindManager:
    def __init__(self):
        self.simple_keybinds = {}
        self.set_single_key_keybind(Actions.ADD_TILE, pygame.K_a)
        self.set_single_key_keybind(Actions.REMOVE_TILE, pygame.K_s)
        self.set_single_key_keybind(Actions.INCREASE_GRID_STEP, pygame.K_PLUS)
        self.set_single_key_keybind(Actions.DECREASE_GRID_STEP, pygame.K_MINUS)

    def set_single_key_keybind(self, action, keybind):
        self.simple_keybinds[keybind] = action

    def get_simple_bind(self, key):
        return self.simple_keybinds[key] if key in self.simple_keybinds else None


KEYBINDS = KeybindManager()
