import pygame
import colorswatch as cs


class GameBoard(object):
    def __init__(self, dimension_x, dimension_y, color = cs.cornflower_blue["pygame"]):
        self.screen_width = dimension_x
        self.screen_height = dimension_y
        self.game_screen = (self.screen_width, self.screen_height)
        self.root = pygame.display.set_mode(self.game_screen)
        self.bg_color = color
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.isInPlay = True


    def update(self):
        self.clock.tick(self.FPS)
        pygame.display.update()
        self.root.fill(self.bg_color)