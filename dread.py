import pygame
import pyautogui
import colorswatch as cs
import random
import os
from enum import Enum
import stages
import player

class GameState(Enum):
    MAIN_MENU = 0
    PAUSE_MENU = 1
    GAME_1 = 2
    GAME_2 = 3
    GAME_3 = 4
    GAME_4 = 5
    GAME_5 = 6
    GAME_6 = 7
    GAME_7 = 8
    GAME_8 = 9
    GAME_9 = 10
    GAME_10 = 11
    GAME_11 = 12
    GAME_12 = 13
    GAME_OVER = 14
    CONTINUE_SCREEN = 15



main_board = stages.GameBoard(640, 480, color = cs.black["pygame"])
player = player.Player(main_board.root, main_board.screen_width / 2, main_board.screen_height / 2)

def draw():
    player.draw()


def update():
    player.update()


def run():
    while main_board.isInPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_board.isInPlay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            main_board.isInPlay = False

        draw()
        update()
        main_board.update()


if __name__ == "__main__":
    run()