#TODO
#outer wall - prevent food from generating off map, detect collisions on wall
#fine tune movement speed and growth rate
#add snake tongue and eyes
#add background?
#add docstrings and better comments
#refactor?
#optimize tail pieces?



import pygame
from snake import Snake
from food import Food

pygame.init()
my_screen = pygame.display.set_mode(size=(1280,720))
pygame.display.set_caption('SNAKE!')
clock = pygame.time.Clock()
running = True
dt = 0

snake = Snake()
snake.screen = my_screen
snake.position = pygame.Vector2(my_screen.get_width() / 2, my_screen.get_height() / 2)

apple = Food()
apple.screen = my_screen


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    my_screen.fill("black")
    snake.draw_snake()
    apple.draw_food()

    snake.handle_keys()
    snake.check_collision(apple, 'food')

    for tail in snake.tails:
        snake.check_collision(tail, 'obstacle')


    pygame.display.flip()
    dt = clock.tick(16)

pygame.quit()

