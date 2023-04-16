import pygame
import colorswatch as cs


class Bullet(object):
    def __init__(self, surface, startX, startY, direction):
        self.surface = surface
        self.direction = direction
        self.color = cs.white["pygame"]
        self.size = 5
        self.speed = 10
        self.bulletRect = pygame.Rect(startX, startY, self.size, self.size)

    def update(self):
        if self.direction == "up":
            self.bulletRect.y -= self.speed
        elif self.direction == "down":
            self.bulletRect.y += self.speed
        elif self.direction == "left":
            self.bulletRect.x -= self.speed
        elif self.direction == "right":
            self.bulletRect.x += self.speed


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.bulletRect)