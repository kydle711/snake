import pygame
import random

class Food:
    def __init__(self):
        self.color = 'dark red'
        self.size = (30,30)
        self.starting_position = (600,600)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.screen = None


    def draw_food(self):
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))

    def get_eaten(self):
        self.rect.update(
            (random.randint(0,self.screen.get_width())),
            (random.randint(0,self.screen.get_height())))
