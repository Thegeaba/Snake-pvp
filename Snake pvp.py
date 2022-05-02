#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
dark_green = (0,100,0)
blue = (50, 153, 213)

dis_width = 1200    # 600
dis_height = 600   # 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by EU')

clock = pygame.time.Clock()

snake_block = 50    # 10
snake_speed = 10    # 15

enemy_snake_block = 50
enemy_snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])

def Enemy_score(score):
    value = score_font.render("                                                                                             Enemy Score: " + str(score), True, dark_green)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def enemy_snake(enemy_snake_block, enemy_snake_list):
    for x in enemy_snake_list:
        pygame.draw.rect(dis, dark_green, [x[0], x[1], enemy_snake_block, enemy_snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_intro = False    ### AICI ???
    game_over = False
    game_close = False

    x1 = dis_width / 3
    y1 = dis_height / 3
    x1_change = 0
    y1_change = 0

    x2 = 2 * dis_width / 3
    y2 = 2 * dis_height / 3
    x2_change = 0
    y2_change = 0

    snake_List = []
    Length_of_snake = 1

    enemy_snake_List = []
    Length_of_enemy_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 50.0) * 50.0
    foody = round(random.randrange(0, dis_height - snake_block) / 50.0) * 50.0

    foodx = round(random.randrange(0, dis_width - enemy_snake_block) / 50.0) * 50.0
    foody = round(random.randrange(0, dis_height - enemy_snake_block) / 50.0) * 50.0

    while not game_over:

        while game_intro == True:
            dis.fill(blue)
            message("Snake v3 \n C - START", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_intro = False
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        while game_close == True:
            dis.fill(blue)
            message("Ai Pierdut! | C-Joaca din Nou | | Q-Quit |", red)
            Your_score(Length_of_snake - 1)
            Enemy_score(Length_of_enemy_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_intro = False
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x2_change = -enemy_snake_block
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = enemy_snake_block
                    y2_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -enemy_snake_block
                    x2_change = 0
                elif event.key == pygame.K_s:
                    y2_change = enemy_snake_block
                    x2_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 or x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True

            
        x1 += x1_change
        y1 += y1_change

        x2 += x2_change
        y2 += y2_change

        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])       # ???
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        pygame.draw.rect(dis, red, [foodx, foody, enemy_snake_block, enemy_snake_block])
        enemy_snake_Head = []
        enemy_snake_Head.append(x2)
        enemy_snake_Head.append(y2)
        enemy_snake_List.append(enemy_snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if len(enemy_snake_List) > Length_of_enemy_snake:
            del enemy_snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in enemy_snake_List[:-1]:
            if x == enemy_snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        enemy_snake(enemy_snake_block, enemy_snake_List)
        
        Your_score(Length_of_snake - 1)
        Enemy_score(Length_of_enemy_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 50.0) * 50.0
            foody = round(random.randrange(0, dis_height - snake_block) / 50.0) * 50.0
            Length_of_snake += 1
        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - enemy_snake_block) / 50.0) * 50.0
            foody = round(random.randrange(0, dis_height - enemy_snake_block) / 50.0) * 50.0
            Length_of_enemy_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()


# In[ ]:





# In[ ]:




