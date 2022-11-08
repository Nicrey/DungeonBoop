import numpy
import pygame

from src.Model.project import Project
from src.Uilib.input_text_view import InputTextView
from src.Uilib.select_list_view import SelectListView
from src.Util.file_manager import FILES
from src.Util.keybind_manager import Actions
from src.Util.setting_manager import Setting, SETTINGS
from src.Views.canvas_view import CanvasView
from src.Views.project_overview import ProjectOverview


class Controller:
    def __init__(self, game):
        self.resized = "NO RESIZE"
        self.current_project = None
        self.projects = FILES.load_projects()
        self.game = game
        self.current_view = ProjectOverview(self.game, self.projects)

    def handle_actions(self, actions, game, canvas):
        for action in actions:
            if action.name == Actions.SCREEN_RESIZE:
                SETTINGS.set(Setting.SCREEN_X, action.values.w)
                SETTINGS.set(Setting.SCREEN_Y, action.values.h)
                self.resized = "RESIZE PENDING"
                continue

            if action.name == Actions.EXIT:
                return None
                # pygame.quit()
                # sys.exit()

            if self.current_view.name == 'CANVAS_VIEW':
                if action.name == Actions.ADD_TILE:
                    canvas.pixel_clicked(action.values.pos, remove=False)
                    continue
                if action.name == Actions.REMOVE_TILE:
                    canvas.pixel_clicked(action.values.pos, remove=True)
                    continue
                if action.name == Actions.INCREASE_GRID_STEP:
                    canvas.increase_grid()
                    continue
                if action.name == Actions.DECREASE_GRID_STEP:
                    canvas.decrease_grid()
                    continue
                if action.name == Actions.RESET:
                    canvas.reset()
                    continue
                if action.name == Actions.SAVE:
                    self.save(canvas)
                    continue
                if action.name == Actions.TO_PROJECT_VIEW:
                    self.switch_to_project_view(canvas)
                    continue
                continue
            if self.current_view.name == 'PROJECT_OVERVIEW':
                if action.name == Actions.SELECT_UP:
                    self.current_view.previous()
                    continue
                if action.name == Actions.SELECT_DOWN:
                    self.current_view.next()
                    continue
                if action.name == Actions.SELECT_ENTER:
                    self.load_canvas_view(self.current_view.get_selected(), canvas)
                    continue
                if action.name == Actions.NEW_PROJECT:
                    self.switch_to_new_project_view()
                    continue
                continue
            if self.current_view.name == 'NEW_PROJECT_VIEW':
                print(action.name, action.values)
                if action.name == Actions.TEXT_INPUT:
                    self.current_view.add_char(action.values['char'])
                    continue
                if action.name == Actions.TEXT_BACK:
                    self.current_view.back()
                    continue
                if action.name == Actions.SELECT_ENTER:
                    self.create_project(self.current_view.get_text(), canvas)
                    continue
                continue

        if self.resized == 'RESIZE PENDING':
            game = pygame.display.set_mode((SETTINGS.get(Setting.SCREEN_X), SETTINGS.get(Setting.SCREEN_Y)),
                                           pygame.RESIZABLE)
            self.resized = 'NO RESIZE'
        return game

    def save(self, canvas):
        pixels = canvas.dungeon_pixels.copy()
        # numpy.savetxt(f'Projects/{self.current_project.name}/save', pixels)
        surface = pygame.Surface((canvas.size_x, canvas.size_y))
        pygame.surfarray.blit_array(surface, pixels)
        # pygame.image.save(surface, f'Projects/{self.current_project.name}/save.bmp')
        FILES.save_project(self.current_project.name, pixels, surface)

    def draw(self):
        width, height = self.game.get_size()
        if self.current_view.name == 'NEW_PROJECT_VIEW':
            self.current_view.render(width/10, height/2)
        else:
            self.current_view.render()
        if self.current_view.name != 'CANVAS_VIEW':
            pygame.display.update()

    def switch_to_project_view(self, canvas):
        self.save(canvas)
        self.current_view = ProjectOverview(self.game, self.projects)

    def switch_to_new_project_view(self):
        self.current_view = InputTextView(self.game,
                                          SETTINGS.get_font(),
                                          SETTINGS.get(Setting.FONT_COLOR),
                                          text="",
                                          allowed_regex=r"[a-zA-Z ]",
                                          name='NEW_PROJECT_VIEW')

    def load_canvas_view(self, project, canvas):
        self.current_project = project
        self.current_view = CanvasView(self.game, canvas, pixels=project.get_pixels())

    def create_project(self, name, canvas):
        project = Project(name)
        self.projects.append(project)
        self.current_view = CanvasView(self.game, canvas, pixels=project.get_pixels())
        self.current_project = project
