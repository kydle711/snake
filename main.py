# TODO
# snake tongue
# background?
# docstrings and better comments
# optimize tail pieces?
# title screen
# difficulty settings
# animation when eating food


import pygame
from snake import Snake, Food, Barrier
def main():
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1280
    SCREEN_BORDER = 10
    BORDER_COLOR = 'dark blue'
    SCREEN_COLOR = 'black'

    pygame.init()
    my_screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('SNAKE!')
    clock = pygame.time.Clock()

    game_running = True
    app_running = True
    dt = 0

    snake = Snake(my_screen, pygame.Vector2(my_screen.get_width() / 2, my_screen.get_height() / 2))
    apple = Food(my_screen)
    my_wall = Barrier(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_BORDER)

    while app_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False
                game_running = False

        while game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    app_running = False
                    game_running = False

            if not app_running:
                break

            my_screen.fill(BORDER_COLOR)

            pygame.draw.rect(my_screen, SCREEN_COLOR, my_wall.rect)

            snake.draw_snake()
            apple.draw_food()

            snake.handle_keys()
            print("handle keys")
            game_running = snake.check_collision(apple, 'food')

            game_running = snake.check_collision(my_wall, 'wall')

            for tail in snake.tails:
                game_running = snake.check_collision(tail, 'obstacle')
                if not game_running:
                    break

            pygame.display.flip()
            dt = clock.tick(18)

    pygame.quit()

if __name__ == '__main__':
    main()