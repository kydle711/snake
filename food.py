import pygame
import random


class Food:
    def __init__(self):
        self.color = 'dark red'
        self.size = (30, 30)
        self.starting_position = (600, 600)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.screen = None

    def draw_food(self):
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))

    def replace(self):
        border = 20
        new_position_x = random.randint(border, self.screen.get_width()-border)
        new_position_y = random.randint(border, self.screen.get_height()-border)
        self.rect.update((new_position_x, new_position_y, *self.size))
