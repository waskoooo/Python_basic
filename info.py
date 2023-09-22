import pygame
import sys
import random

# Инициализация на pygame
pygame.init()

# Размери на прозореца
width = 640
height = 480

# Цветове
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Създаване на прозорец
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змия")

# Размер на блока
block_size = 20

# Инициализация на часовника
clock = pygame.time.Clock()

# Инициализация на шрифта
font = pygame.font.SysFont(None, 36)

# Функция за изчертаване на змията
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], block_size, block_size))

# Главен цикъл
def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake = [(x, y)]

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            screen.fill(black)
            message = font.render("Изгубихте! Натиснете C за нова игра или Q за изход.", True, white)
            screen.blit(message, (width // 4, height // 3))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.fill(black)
        pygame.draw.rect(screen, red, (food_x, food_y, block_size, block_size))

        snake.append((x, y))
        if len(snake) > 1:
            snake = snake[-len(snake) + 1:]

        for segment in snake[:-1]:
            if segment == (x, y):
                game_close = True

        draw_snake(snake)

        pygame.display.flip()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

        clock.tick(15)

    pygame.quit()
    sys.exit()

game_loop()
