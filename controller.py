import numpy
import pygame
from keybind_manager import Actions
from setting_manager import Setting, SETTINGS


class Controller:
    def __init__(self):
        self.resized = "NO RESIZE"
        self.current_project = "Test"

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
            if action.name == Actions.RESET:
                canvas.reset()
            if action.name == Actions.SAVE:
                self.save(canvas.dungeon_pixels.copy(), canvas)
        if self.resized == 'RESIZE PENDING':
            game = pygame.display.set_mode((SETTINGS.get(Setting.SCREEN_X), SETTINGS.get(Setting.SCREEN_Y)),
                                           pygame.RESIZABLE)
            self.resized = 'NO RESIZE'
        return game

    def save(self, pixels, canvas):
        numpy.savetxt(f'Projects/{self.current_project}/save', pixels)
        surface = pygame.Surface((canvas.size_x, canvas.size_y))
        pygame.surfarray.blit_array(surface, pixels)
        pygame.image.save(surface, f'Projects/{self.current_project}/save.bmp')

