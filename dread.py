import pygame
import pyautogui
import colorswatch as cs
import random
import os
from enum import Enum
import stages
import player
import enemy as en
import city

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


ENEMY_SPACING = 10

main_board = stages.GameBoard(640, 480, color = cs.black["pygame"])
player = player.Player(main_board.root, main_board.screen_width / 2, main_board.screen_height / 2)
enemy_list = []
machi = city.City(main_board.root, 0, main_board.screen_height - 60 * 3)

level = 1

def roll():
    startX, startY = 0, 0
    if random.randrange(1, 5) == 1:
        startX = -20
        startY = random.randrange(0, main_board.screen_height)
    if random.randrange(1, 5) == 2:
        startX = main_board.screen_width + 20
        startY = random.randrange(0, main_board.screen_height)
    if random.randrange(1, 5) == 3:
        startX = random.randrange(0, main_board.screen_width)
        startY = -20
    if random.randrange(1, 5) == 4:
        startX = random.randrange(0, main_board.screen_width)
        startY = main_board.screen_height + 20

    return startX, startY


def clone_enemy():
    x, y = roll()
    enemy = en.Enemy(main_board.root, x, y)
    enemy_list.append(enemy)


def get_enemies(level):
    while len(enemy_list) <= level:
        clone_enemy()


def level_up(new_level):
    global level
    level = new_level
    get_enemies(level)
    return level

def draw():
    machi.draw()
    player.draw()

    for enemy in enemy_list:
        enemy.draw()



def update():

    for enemy in enemy_list:
        enemy.chase(player.playerRect.x)
        if enemy.rect.y >= main_board.screen_height - enemy.size:
            enemy.take_hit()

        for bullets in player.bullet_list:
            if bullets.bulletRect.colliderect(enemy.rect):
                enemy.take_hit()
                player.bullet_list.remove(bullets)

        for bricks in machi.brick_list:
            if bricks.colliderect(enemy.rect):
                bricks.y += 2
                if bricks.y >= main_board.screen_height:
                    machi.brick_list.remove(bricks)
        for windows in machi.window_list:
            if windows.colliderect(enemy.rect):
                windows.y += 2
                if windows.y >= main_board.screen_height:
                    machi.window_list.remove(windows)
        for shader in machi.shade_list:
            if shader.colliderect(enemy.rect):
                shader.y += 2
                if shader.y >= main_board.screen_height:
                    machi.shade_list.remove(shader)


    for bullets in player.bullet_list:
        for bricks in machi.brick_list:
            if bullets.bulletRect.colliderect(bricks):
                machi.brick_list.remove(bricks)
        for windows in machi.window_list:
            if bullets.bulletRect.colliderect(windows):
                machi.window_list.remove(windows)
        for shader in machi.shade_list:
            if bullets.bulletRect.colliderect(shader):
                machi.shade_list.remove(shader)




    player.update()




def run():
    level_up(1)
    machi.build_building()


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