import pygame

from keybind_manager import Actions
from setting_manager import Setting, SETTINGS


class Controller:
    def __init__(self):
        self.resized = "NO RESIZE"

    def handle_actions(self, actions, game, canvas):
        for action in actions:
            if action.name == Actions.SCREEN_RESIZE:
                SETTINGS.set(Setting.SCREEN_X, action.values.w)
                SETTINGS.set(Setting.SCREEN_Y, action.values.h)
                self.resized = "RESIZE PENDING"

            if action.name == Actions.EXIT:
                return None
                # pygame.quit()
                # sys.exit()

            if action.name == Actions.ADD_TILE:
                canvas.pixel_clicked(action.values.pos, remove=False)
            if action.name == Actions.REMOVE_TILE:
                canvas.pixel_clicked(action.values.pos, remove=True)
            if action.name == Actions.INCREASE_GRID_STEP:
                canvas.increase_grid()
            if action.name == Actions.DECREASE_GRID_STEP:
                canvas.decrease_grid()
        if self.resized == 'RESIZE PENDING':
            game = pygame.display.set_mode((SETTINGS.get(Setting.SCREEN_X), SETTINGS.get(Setting.SCREEN_Y)),
                                           pygame.RESIZABLE)
            self.resized = 'NO RESIZE'
        return game
