import pygame

from src.Util.keybind_manager import Actions, Action, KEYBINDS


class InputHandler:
    def __init__(self):
        self.mouse_left_down = False
        self.mouse_right_down = False
        self.add_tile_active = False
        self.remove_tile_active = False

    def handle_event(self):
        actions = []
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys:
        #     handler.handle_key_still_pressed(pressed_keys)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_action = self.handle_keydown(event)
                if key_action:
                    actions.append(key_action)

            if event.type == pygame.KEYUP:
                self.handle_keyup(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    actions.append(Action(Actions.ADD_TILE, event))
                    self.mouse_left_down = True
                if event.button == 3:
                    actions.append(Action(Actions.REMOVE_TILE, event))
                    self.mouse_right_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_left_down = False
                if event.button == 3:
                    self.mouse_right_down = False

            if event.type == pygame.MOUSEMOTION:
                if self.mouse_left_down or self.add_tile_active:
                    actions.append(Action(Actions.ADD_TILE, event))
                if self.mouse_right_down or self.remove_tile_active:
                    actions.append(Action(Actions.REMOVE_TILE, event))

            if event.type == pygame.QUIT:
                actions.append(Action(Actions.EXIT, {}))

            if event.type == pygame.VIDEORESIZE:
                actions.append(Action(Actions.SCREEN_RESIZE, event))

        return actions

    def handle_keydown(self, event):
        mods = pygame.key.get_mods()
        strg = mods & pygame.KMOD_CTRL
        key = event.key
        print(pygame.key.name(key))
        if strg:
            action = KEYBINDS.get_control_bind(key)
        else:
            action = KEYBINDS.get_simple_bind(key)
        if action == Actions.ADD_TILE:
            self.add_tile_active = True
            return Action(action, MouseData(pygame.mouse.get_pos()))
        if action == Actions.REMOVE_TILE:
            self.remove_tile_active = True
            return Action(action, MouseData(pygame.mouse.get_pos()))
        if action is None:
            return Action(Actions.TEXT_INPUT, {'char': pygame.key.name(key)})
        print(action)
        return Action(action, event)

    def handle_keyup(self, event):
        key = event.key
        action = KEYBINDS.get_simple_bind(key)
        if action == Actions.ADD_TILE:
            self.add_tile_active = False
        if action == Actions.REMOVE_TILE:
            self.remove_tile_active = False

class MouseData:
    def __init__(self, pos):
        self.pos = pos
