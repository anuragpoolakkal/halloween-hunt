from http.client import PROXY_AUTHENTICATION_REQUIRED
import pygame
import os

pygame.init()

#Screen size
width = 1200
height = 800

win = pygame.display.set_mode((width, height))
bg_img = pygame.image.load(os.path.join("images", "halloween.png"))
bg = pygame.transform.scale(bg_img, (width, height))

i = 0

run = True

vel_x = 10
vel_y = 10

jump = False

run = True

p_width = 50
p_height = 90
player = pygame.image.load(os.path.join("images/player.png"))
player = pygame.transform.scale(player, (p_width, p_height))
player.convert()

heart = pygame.image.load(os.path.join("images/heart.png"))
heart = pygame.transform.scale(heart, (60, 60))

floor = pygame.image.load(os.path.join("images/floor.png"))
floor = pygame.transform.scale(floor, (width, 50))

step = pygame.image.load(os.path.join("images/floating_floor.png"))

pumpkin = pygame.image.load(os.path.join("images/pumpkin.png"))
pumpkin = pygame.transform.scale(pumpkin, (30, 30))

pumpkins = [];

player_x = 20
player_y = height - p_height

floor_x = 0
floor_y = height - 55

steps_height = [50, 50, 50, 50]
steps_width = [width * 0.1, width * 0.1, width * 0.2, width * 0.2]
steps_y = [height - 200, height - 200, height - 200, height - 400]
steps_x = [0, 400, 600, 0]

hearts = 3
hearts_x = [170, 120, 70]

while run:
    # pygame.time.delay(10)
    #Setup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))

    #Lives
    for i in range(hearts):
        win.blit(heart, (width - hearts_x[i], 30))

    #Floor
    win.blit(floor, (floor_x, floor_y))

    #Steps
    for x in range(len(steps_x)):
        step = pygame.transform.scale(step, (steps_width[x], steps_height[x]))
        # if(player)

        # if(steps_x[x] < width):
        #     steps_x[x] += 5
        # else:
        #     while(steps_x[x] >= 0):
        #         steps_x[x] -= 5
        
        # if(player_y <= steps_y[x]):
        #     player_y = steps_y[x]


        # steps_x[x] =  steps_x[x] + 10 if steps_x[x] < width else steps_x[x] - 10 
        if(jump):
            if(player_x >= steps_x[x] and player_x <= steps_x[x]):
                player_y = steps_y[x] + p_height

        win.blit(step, (steps_x[x], steps_y[x]))

    #Pumpkin
    for i in range(10):
        win.blit(pumpkin, (i * 10, i+10));

    #Player
    win.blit(player, (player_x, player_y))
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and player_x > 0:
        player_x -= vel_x
    if userInput[pygame.K_RIGHT] and player_x < width:
        player_x += vel_x

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        player_y -= vel_y * 4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    #Floor collision
    if((player_y + p_height) >= floor_y):
        player_y -= 30


    #Game over condition
    if hearts <= 0:
        print("Game Over")
        pygame.quit()
    
    
    pygame.display.update()

pygame.quit()