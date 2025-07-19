import pygame
import time
import random

pygame.init()

red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

win_width = 600
win_heigth = 400
window = pygame.display.set_mode((win_width, win_heigth))
pygame.display.set_caption("Snake Game")
time.sleep(1)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

def user_score(score):
    number = score_font.render("Score : " + str(score), True, red)
    window.blit(number, [0, 0])

def game_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def message(msg):
    msg_text = font_style.render(msg, True, red)
    window.blit(msg_text, [win_width / 18, win_heigth / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_heigth / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_heigth - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(grey)
            message("You lost! Press P to play again or Q to quit.")
            user_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        x1 += x1_change
        y1 += y1_change

        if x1 >= win_width or x1 < 0 or y1 >= win_heigth or y1 < 0:
            game_close = True

        window.fill(grey)
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        game_snake(snake_block, snake_list)
        user_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_heigth - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
