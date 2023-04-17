import pygame
import colorswatch as cs
import random

color_list = [cs.fuchsia["pygame"], cs.white["pygame"], cs.blue["pygame"], cs.shit["pygame"], cs.night_gray["pygame"], cs.purple_rain["pygame"]]

class Enemy(object):
    def __init__(self, surface, startX, startY, color = color_list[0]):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.color = color
        self.size = 20
        self.speed = 2
        self.rect = pygame.Rect(self.startX, self.startY, self.size, self.size)
        self.coupler_rect = pygame.Rect(self.startX, self.startY - 2, self.size, self.size)
        self.direction = "left"
        self.isHit = False
        self.isSettled = False


    def chase(self, target_x):
        if not self.isSettled:
            if self.rect.x > target_x:
                self.rect.x -= self.speed
                self.coupler_rect.x -= self.speed
            if self.rect.x < target_x:
                self.rect.x += self.speed
                self.coupler_rect.x += self.speed

            self.rect.y += self.speed
            self.coupler_rect.y += self.speed

        if self.isHit:
            self.rect.x = random.randrange(0, 640)
            self.rect.y = 0
            self.color = color_list[random.randrange(0, len(color_list))]
            self.coupler_rect.x = self.rect.x
            self.coupler_rect.y = self.rect.y - 2
            self.isHit = False
            self.isSettled = False





    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)