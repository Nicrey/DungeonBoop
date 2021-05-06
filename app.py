import time
import pygame
from numpy import average

import drawer
from setting_manager import Setting, SETTINGS
import canvas
import controller
from input_handler import InputHandler

pygame.init()
pygame.font.init()

# General Init
GAME = pygame.display.set_mode((SETTINGS.get(Setting.SCREEN_X), SETTINGS.get(Setting.SCREEN_Y)), pygame.RESIZABLE)
pygame.display.set_caption(f"{SETTINGS.get(Setting.NAME)} {SETTINGS.get(Setting.VERSION)}")
clock = pygame.time.Clock()
handler = InputHandler()
controller = controller.Controller()
# Font and Fitting Cursor
draw_canvas = canvas.Canvas(SETTINGS.get(Setting.SCREEN_X), SETTINGS.get(Setting.SCREEN_Y))
start_time = time.perf_counter()


handle_event_times = []
handle_action_times = []
draw_times = []
while True:
    loop_start = time.perf_counter()
    ###############################################
    #               EVENT HANDLING
    ##############################################
    actions = handler.handle_event()
    first_time = time.perf_counter() - loop_start

    start = time.perf_counter()
    GAME = controller.handle_actions(actions, GAME, draw_canvas)
    second_time = time.perf_counter() - start
    if GAME is None:
        break
    ###################################################
    #                DRAWING
    ###################################################
    start = time.perf_counter()
    drawer.draw(GAME, draw_canvas)
    third_time = time.perf_counter() - start
    handle_action_times.append(second_time)
    handle_event_times.append(first_time)
    draw_times.append(third_time)
    # print(clock.get_fps())
    clock.tick(SETTINGS.get(Setting.FPS))

print("Exited")
print(handle_event_times)
print(handle_action_times)
print(draw_times)
print(average(handle_event_times))
print(average(handle_action_times))
print(average(draw_times))