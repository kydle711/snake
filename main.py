# TODO
# snake tongue?
# background?
# title screen
# difficulty settings
# animation when eating food


import pygame
from snake import Snake, Food, Barrier


def main():
    SCREEN_HEIGHT = 720              # Main settings
    SCREEN_WIDTH = 1280
    SCREEN_BORDER = 10
    BORDER_COLOR = 'dark blue'
    SCREEN_COLOR = 'black'

    pygame.init()
    my_screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))     # set up screen and window
    pygame.display.set_caption('SNAKE!')
    clock = pygame.time.Clock()

    game_running = True  # False when snake runs in to tail or wall
    app_running = True  # False when closing window to exit game

    snake = Snake(my_screen, pygame.Vector2(my_screen.get_width() / 2, my_screen.get_height() / 2))
    apple = Food(my_screen)
    my_wall = Barrier(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_BORDER)

    while app_running:     # Outer while loop to keep app open even after crashing into something

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False
                game_running = False

        while game_running:     # Inner loop for gameplay functions

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
            game_running = snake.check_collision(apple, 'food')

            game_running = snake.check_collision(my_wall, 'wall')

            for tail in snake.tails:
                game_running = snake.check_collision(tail, 'obstacle')
                if not game_running:      # If a single tail collision is detected, end the loop
                    break

            pygame.display.flip()
            clock.tick(18)

    pygame.quit()         # App will close when outer while loop is exited


if __name__ == '__main__':
    main()
