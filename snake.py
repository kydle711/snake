import pygame
import random


class Snake:
    """ Snake class for the head. Also holds a list of tailpieces as snake grows. """
    def __init__(self, screen, starting_position):
        self.length = 1
        self.size = (20, 20)
        self.starting_position = starting_position
        self.color = 'green'
        self.speed = 22
        self.direction = (0, 0)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.last_position = (0, 0)
        self.tails = []
        self.screen = screen
        self.facing = 'n'
        self.eye_radius = 3
        self.eye_color = 'black'

    def handle_keys(self):
        """ Check for key presses and change direction accordingly. """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self._move_up()
        if keys[pygame.K_s]:
            self._move_down()
        if keys[pygame.K_a]:
            self._move_left()
        if keys[pygame.K_d]:
            self._move_right()

    def draw_snake(self):
        """ Set last position as a reference for subsequent pieces of the snake. Update rect.x and rect.y
        according to the direction snake is heading. Then draw the snake and tail."""
        self.last_position = (self.rect.x, self.rect.y)
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))

        self._draw_head()

        for tail in self.tails:
            tail.draw_tail()

    def _draw_left_eye(self, orientation):
        """ Draws left eye according to orientation of the snake. """
        head_position = (self.rect.x, self.rect.y)
        left_eye_coords = (head_position[0] + orientation[0][0],
                           head_position[1] + orientation[0][1])
        pygame.draw.circle(self.screen, self.eye_color, left_eye_coords, self.eye_radius)

    def _draw_right_eye(self, orientation):
        """ Draws the right eye as well. """
        head_position = (self.rect.x, self.rect.y)
        right_eye_coords = (head_position[0] + orientation[1][0],
                            head_position[1] + orientation[1][1])
        pygame.draw.circle(self.screen, self.eye_color, right_eye_coords, self.eye_radius)

    def _draw_head(self):
        """ Consolidates drawing the eyes according to the orientation into a single func call.
        Will support further details to be added later. """
        orientation_dict = {'n': ((5, 5), (15, 5)),
                            's': ((5, 15), (15, 15)),
                            'e': ((15, 5), (15, 15)),
                            'w': ((5, 5), (5, 15))}

        current_orientation = orientation_dict[self.facing]
        self._draw_left_eye(current_orientation)
        self._draw_right_eye(current_orientation)

    def _move_down(self):
        if self.direction[1] == 0:
            self.direction = (0, self.speed)
            self.facing = 's'

    def _move_up(self):
        if self.direction[1] == 0:
            self.direction = (0, -self.speed)
            self.facing = 'n'

    def _move_left(self):
        if self.direction[0] == 0:
            self.direction = (-self.speed, 0)
            self.facing = 'w'

    def _move_right(self):
        if self.direction[0] == 0:
            self.direction = (self.speed, 0)
            self.facing = 'e'

    def _add_tail(self, head_node):
        new_tail = Tail(head_node)
        self.tails.append(new_tail)
        self.length += 1

    def _eat_food(self):
        if self.length > 200:
            for i in range(3):
                self._add_tail(self.tails[-1])
        elif 1 < self.length < 200:
            for i in range(5):
                self._add_tail(self.tails[-1])
        else:
            self._add_tail(self)
            for i in range(4):
                self._add_tail(self.tails[-1])

    def check_collision(self, other_object, collision_type):
        """ Returns 'True' or 'False for the main game loop depending on collision types. """
        if collision_type == 'wall':
            if not pygame.Rect.contains(other_object.rect, self):
                print('wall collision')
                self.speed = 0
                return False
        else:
            if pygame.Rect.colliderect(self.rect, other_object.rect):
                if collision_type == 'food':
                    print('ate food')
                    self._eat_food()
                    other_object.replace()
                    return True

                elif collision_type == 'obstacle':
                    print('tail collision')
                    self.speed = 0
                    return False
        return True


class Tail:
    """ A class to hold tailpieces and link them together so that they can follow the head."""

    def __init__(self, head_node):
        self.rect = pygame.Rect(*head_node.last_position, *head_node.size)
        self.color = head_node.color
        self.screen = head_node.screen
        self.size = head_node.size
        self.leading_node = head_node
        self.last_position = head_node.last_position

    def draw_tail(self):
        """ Draw each tail based off its head node's last position attr. """
        self.last_position = (self.rect.x, self.rect.y)
        self.rect.x = self.leading_node.last_position[0]
        self.rect.y = self.leading_node.last_position[1]
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))


class Food:
    """ A class for the food that is eaten. Will redraw each time it is eaten to a random location."""
    def __init__(self, screen):
        self.color = 'red'
        self.size = (30, 30)
        self.starting_position = (600, 600)
        self.rect = pygame.Rect(*self.starting_position, *self.size)
        self.screen = screen
        self.food_counter = 0

    def draw_food(self):
        pygame.draw.rect(self.screen, self.color, (self.rect.x, self.rect.y, *self.size))

    def replace(self):
        """ Update the position after the food is eaten. """
        border = 50
        new_position_x = random.randint(border, self.screen.get_width() - border)
        new_position_y = random.randint(border, self.screen.get_height() - border)
        self.rect.update((new_position_x, new_position_y, *self.size))
        self.food_counter += 1

    def get_food_counter(self):
        """ Keep track of food pieces that are eaten for displaying score in future updates."""
        return self.food_counter


class Barrier:
    """ A class for creating a main rect. Gameplay occurs within this rect, and leaving the rect
    equates to 'running into the wall' """
    def __init__(self, height, width, border):
        self.rect = pygame.Rect((border, border), (width - 2 * border, height - 2 * border))


