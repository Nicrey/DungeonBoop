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
    NEW_PROJECT = 8
    TO_PROJECT_VIEW = 9
    TEXT_INPUT = 10
    TEXT_BACK = 11
    TEXT_ENTER = 12
    SELECT_DOWN = 13
    SELECT_UP = 14
    SELECT_ENTER = 15


class Action:
    def __init__(self, action: Actions, values: {}):
        self.name = action
        self.values = values


class KeybindManager:
    def __init__(self):
        self.reverse_lookup = {}
        self.simple_keybinds = {}
        # Canvas View
        self.set_single_key_keybind(Actions.ADD_TILE, pygame.K_a)
        self.set_single_key_keybind(Actions.REMOVE_TILE, pygame.K_s)
        self.set_single_key_keybind(Actions.INCREASE_GRID_STEP, pygame.K_PLUS)
        self.set_single_key_keybind(Actions.DECREASE_GRID_STEP, pygame.K_MINUS)
        # Project Overview/ New Project
        self.set_single_key_keybind(Actions.SELECT_UP, pygame.K_UP)
        self.set_single_key_keybind(Actions.SELECT_DOWN, pygame.K_DOWN)
        self.set_single_key_keybind(Actions.TEXT_ENTER, pygame.K_RETURN)
        self.set_single_key_keybind(Actions.SELECT_ENTER, pygame.K_RETURN)
        self.set_single_key_keybind(Actions.TEXT_BACK, pygame.K_BACKSPACE)

        self.control_keybinds = {}
        self.set_control_key_keybind(Actions.RESET, pygame.K_r)
        self.set_control_key_keybind(Actions.SAVE, pygame.K_s)
        self.set_control_key_keybind(Actions.NEW_PROJECT, pygame.K_c)
        self.set_control_key_keybind(Actions.TO_PROJECT_VIEW, pygame.K_p)
        # Project Overview / New Project
        self.reverse_lookup[Actions.NEW_PROJECT] = 'STRG + C'

        self.alt_keybinds = {}
        self.shift_keybinds = {}

    def set_single_key_keybind(self, action, keybind):
        self.simple_keybinds[keybind] = action

    def set_control_key_keybind(self, action, keybind):
        self.control_keybinds[keybind] = action

    def get_control_bind(self, key):
        return self.control_keybinds[key] if key in self.control_keybinds else None

    def get_simple_bind(self, key):
        return self.simple_keybinds[key] if key in self.simple_keybinds else None


KEYBINDS = KeybindManager()
