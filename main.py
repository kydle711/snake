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
apple = Food()
apple.screen = my_screen
snake.position = pygame.Vector2(my_screen.get_width() / 2, my_screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    my_screen.fill("black")

    snake.slither()
    snake.draw_snake()
    apple.draw_food()
    snake.check_collision(apple.rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.move_up()
    if keys[pygame.K_s]:
        snake.move_down()
    if keys[pygame.K_a]:
        snake.move_left()
    if keys[pygame.K_d]:
        snake.move_right()

    pygame.display.flip()
    dt = clock.tick(15)

pygame.quit()

