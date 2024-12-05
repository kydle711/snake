import pygame


class Snake:
    def __init__(self):
        self.length = 1
        self.size = (30,30)
        self.starting_position= (300,300)
        self.color = 'dark green'
        self.speed = 24
        self.direction = (0, 0)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.last_position = (0,0)
        self.tails = []
        self.screen = None


    def slither(self):
        self.last_position = (self.rect.x, self.rect.y)
        self.rect.y += self.direction[1]
        self.rect.x += self.direction[0]
        for tail in self.tails:
            tail.rect.x, tail.rect.y = self.last_position


    def draw_snake(self):
        pygame.draw.rect(self.screen, self.color,(self.rect.x, self.rect.y, *self.size))

        for tail in self.tails:
            tail.draw_tail()


    def move_down(self):
        self.direction = (0,self.speed)

    def move_up(self):
        self.direction = (0,-self.speed)

    def move_left(self):
        self.direction = (-self.speed,0)

    def move_right(self):
        self.direction = (self.speed,0)

    def _eat_food(self):
        head_position = (self.rect.x, self.rect.y)
        self.length += 1
        new_tail = Tail(self)
        self.tails.append(new_tail)


    def check_collision(self, other_rect):
        collision = pygame.Rect.colliderect(self.rect, other_rect)
        if collision:
            self._eat_food()


class Tail:

    def __init__(self, head_node):
        self.rect = pygame.Rect(*head_node.last_position, *head_node.size)
        self.color = head_node.color
        self.screen = head_node.screen
        self.size = head_node.size
        self.leading_node = head_node.rect


    def draw_tail(self):
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))



