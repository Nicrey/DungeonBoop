import pygame

from keybind_manager import Actions, Action


class InputHandler:
    def __init__(self):
        self.mouse_left_down = False
        self.mouse_right_down = False

    def handle_event(self):
        actions = []
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys:
        #     handler.handle_key_still_pressed(pressed_keys)
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     handler.handle_keydown(event.key, event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    actions.append(Action(Actions.MOUSE_LEFT_EVENT, event))
                    self.mouse_left_down = True
                if event.button == 3:
                    actions.append(Action(Actions.MOUSE_RIGHT_EVENT, event))
                    self.mouse_right_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_left_down = False
                if event.button == 3:
                    self.mouse_right_down = False

            if event.type == pygame.MOUSEMOTION:
                if self.mouse_left_down:
                    actions.append(Action(Actions.MOUSE_LEFT_EVENT, event))
                if self.mouse_right_down:
                    actions.append(Action(Actions.MOUSE_RIGHT_EVENT, event))

            if event.type == pygame.QUIT:
                actions.append(Action(Actions.EXIT, {}))

            if event.type == pygame.VIDEORESIZE:
                actions.append(Action(Actions.SCREEN_RESIZE, event))

        return actions