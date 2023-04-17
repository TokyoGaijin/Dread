import pygame
import colorswatch as cs
import bullet
from enum import Enum

class PlayerStates(Enum):
    ALIVE = 0
    DEAD = 1


class ControlState(Enum):
    DEV = 0
    GAME = 1


class MoveStates(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player(object):
    def __init__(self, surface, startX, startY, x_limit = 640, y_limit = 480):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.size = 10
        self.speed = 3
        self.color = cs.red["pygame"]
        self.playerRect = pygame.Rect(self.startX, self.startY, self.size, self.size)
        self.current_state = PlayerStates.ALIVE
        self.x_bound = x_limit
        self.y_bound = y_limit
        self.controlState = ControlState.GAME
        self.direction = "left"
        self.bullet_list = []
        self.IMPACT_EVENT = pygame.USEREVENT + 1


    def move(self, direction):
        if direction == "up":
            self.playerRect.y -= self.speed
        if direction == "down":
            self.playerRect.y += self.speed
        if direction == "left":
            self.playerRect.x -= self.speed
        if direction == "right":
            self.playerRect.x += self.speed





    def update(self):
        keys = pygame.key.get_pressed()

        # Mode Change
        # TODO: Delete before production
        if keys[pygame.K_m]:
            if self.controlState == ControlState.GAME:
                self.controlState = ControlState.DEV
            else:
                self.controlState = ControlState.GAME

        if keys[pygame.K_UP]:
            self.direction = "up"
        if keys[pygame.K_DOWN]:
            self.direction = "down"
        if keys[pygame.K_LEFT]:
            self.direction = "left"
        if keys[pygame.K_RIGHT]:
            self.direction = "right"

        if keys[pygame.K_SPACE]:
            if len(self.bullet_list) < 1:
                self.bullet_list.append(bullet.Bullet(self.surface, self.playerRect.x + self.size / 2, self.playerRect.y + self.size / 2, self.direction))

        for bullets in self.bullet_list:
            bullets.update()
            if bullets.bulletRect.x <= 0 or bullets.bulletRect.x >= self.x_bound:
                self.bullet_list.remove(bullets)
            if bullets.bulletRect.y <= 0 or bullets.bulletRect.y >= self.y_bound:
                self.bullet_list.remove(bullets)

        if self.controlState == ControlState.DEV:
            if keys[pygame.K_UP]:
                self.move("up")
            if keys[pygame.K_DOWN]:
                self.move("down")
            if keys[pygame.K_LEFT]:
                self.move("left")
            if keys[pygame.K_RIGHT]:
                self.move("right")
        if self.controlState == ControlState.GAME:
            self.move(self.direction)

        if self.playerRect.x <= 0:
            self.playerRect.x = self.x_bound - self.size
        if self.playerRect.x >= self.x_bound:
            self.playerRect.x = 0

        if self.playerRect.y <= 0:
            self.playerRect.y = self.y_bound - self.size
        if self.playerRect.y >= self.y_bound:
            self.playerRect.y = 0


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.playerRect)
        for bullets in self.bullet_list:
            bullets.draw()