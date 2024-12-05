import pygame


class Snake:
    def __init__(self):
        self.length = 1
        self.size = (20, 20)
        self.starting_position = (300, 300)
        self.color = 'dark green'
        self.speed = 25
        self.direction = (0, 0)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.last_position = (0, 0)
        self.tails = []
        self.screen = None

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()


    def draw_snake(self):
        self.last_position = (self.rect.x, self.rect.y)
        self.rect.y += self.direction[1]
        self.rect.x += self.direction[0]
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))

        for tail in self.tails:
            tail.draw_tail()

    def move_down(self):
        if self.direction[1] == 0:
            self.direction = (0, self.speed)

    def move_up(self):
        if self.direction[1] == 0:
            self.direction = (0, -self.speed)

    def move_left(self):
        if self.direction[0] == 0:
            self.direction = (-self.speed, 0)

    def move_right(self):
        if self.direction[0] == 0:
            self.direction = (self.speed, 0)

    def _eat_food(self):
        if self.length > 1:
            new_tail = Tail(self.tails[-1])
        else:
            new_tail = Tail(self)

        self.tails.append(new_tail)
        self.length += 1

    def check_collision(self, other_object, collision_type):
            collision = pygame.Rect.colliderect(self.rect, other_object.rect)
            if collision:
                if collision_type == 'food':
                    self._eat_food()
                    other_object.replace()
                elif collision_type == 'obstacle':
                    self._end_game()


    def _end_game(self):
        self.speed = 0



class Tail:

    def __init__(self, head_node):
        self.rect = pygame.Rect(*head_node.last_position, *head_node.size)
        self.color = head_node.color
        self.screen = head_node.screen
        self.size = head_node.size
        self.leading_node = head_node
        self.last_position = None

    def draw_tail(self):
        self.last_position = (self.rect.x, self.rect.y)
        self.rect.x = self.leading_node.last_position[0]
        self.rect.y = self.leading_node.last_position[1]
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))
