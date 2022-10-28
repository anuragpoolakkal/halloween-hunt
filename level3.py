from http.client import PROXY_AUTHENTICATION_REQUIRED
import pygame
import os
from random import randrange
from menu import *

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

def level3():
    pygame.init()

    # Screen size
    width = 1200
    height = 800

    win = pygame.display.set_mode((width, height))
    bg_img = pygame.image.load(os.path.join("images", "bg-3.png"))
    bg = pygame.transform.scale(bg_img, (width, height))

    i = 0

    run = True

    vel_x = 10
    vel_y = 10

    jump = False

    run = True

    p_width = 50
    p_height = 90
    player = pygame.image.load(os.path.join("images/player_r.png"))
    player = pygame.transform.scale(player, (p_width, p_height))
    player.convert()

    heart = pygame.image.load(os.path.join("images/heart.png"))
    heart = pygame.transform.scale(heart, (60, 60))

    score_icon = pygame.image.load(os.path.join("images/pumpkin.png"))
    score_icon = pygame.transform.scale(score_icon, (40, 40))

    floor = pygame.image.load(os.path.join("images/floor.png"))
    floor = pygame.transform.scale(floor, (width, 50))

    step = pygame.image.load(os.path.join("images/floating_floor.png"))

    pumpkin = pygame.image.load(os.path.join("images/pumpkin.png"))
    pumpkin = pygame.transform.scale(pumpkin, (60, 60))

    bat = pygame.image.load(os.path.join("images/bat.png"))
    bat = pygame.transform.scale(bat, (30, 30))

    pumpkins = []

    player_x = 20
    player_y = height - p_height

    floor_x = 0
    floor_y = height - 55

    steps_height = [50, 50, 50, 50]
    steps_width = [width * 0.1, width * 0.1, width * 0.2, width * 0.2]
    steps_y = [floor_y - 200, floor_y - 200, floor_y - 200, floor_y - 400]
    steps_x = [0, 400, 800, 0]

    hearts = 3
    hearts_x = [170, 120, 70]

    enemy = pygame.image.load(os.path.join("images/hoodieskelton.png"))
    enemy = pygame.transform.scale(enemy, (60, 60))

    # background music
    music = pygame.mixer.Sound('music/halloween_music.mp3')
    music.set_volume(0.05)
    music.play()

    enemy_count = 6

    enemies_y = [] 
    enemies_x = []
    for i in range(enemy_count):
        enemies_x.append(randrange(0, width))
        enemies_y.append(randrange(-200, 0))

    pumpkin_count = 5
    pumpkins_x = []
    pumpkins_y = []
    for i in range(pumpkin_count):
        pumpkins_x.append(randrange(0, width))
        pumpkins_y.append(randrange(-200, 0))

    score = 0

    while run:
        # pygame.time.delay(10)
        # player = pygame.image.load(os.path.join("images/player_r.png"))
        # Setup
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))
        win.blit(bg, (0, 0))

        # Steps
        # for x in range(len(steps_x)):
        #     step = pygame.transform.scale(step, (steps_width[x], steps_height[x]))
        #     win.blit(step, (steps_x[x], steps_y[x]))

        # Player
        win.blit(player, (player_x, player_y))
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT] and player_x > 0:
            player_x -= vel_x

        if userInput[pygame.K_RIGHT] and player_x < width - p_width:
            player_x += vel_x

        if jump is False and userInput[pygame.K_SPACE]:
            jump = True
        if jump is True:
            player_y -= vel_y * 4
            vel_y -= 1
            if vel_y < -10:
                jump = False
                vel_y = 10

        # Lives
        for i in range(hearts):
            win.blit(heart, (width - hearts_x[i], 30))

        win.blit(floor, (floor_x, floor_y))

        #Score
        win.blit(score_icon, (width - hearts_x[0], 100))
        myfont = pygame.font.SysFont("Segoe UI", 30)
        # apply it to text on a label
        label = myfont.render(str(score), 1, white)
        # put the label object on the screen at point x=100, y=100
        win.blit(label, (width - hearts_x[0] + 50, 100))

        # Pumpkin
        for i in range(pumpkin_count):
            win.blit(pumpkin, (pumpkins_x[i], pumpkins_y[i]))
            pumpkins_y[i] += 5

        if(pumpkins_y[i] > height):
            pumpkins_x.clear()
            pumpkins_y.clear()
            for i in range(pumpkin_count):
                pumpkins_x.append(randrange(0, width))
                pumpkins_y.append(randrange(-100, 0))

        # Bat
        for i in range(1):
            win.blit(bat, (randrange(0, width), 100))
            win.blit(bat, (randrange(0, width), 200))

        # Enemies
        for i in range(enemy_count):
            win.blit(enemy, (enemies_x[i], enemies_y[i]))
            enemies_y[i] += 5

            if(enemies_y[i] > height):
                enemies_x.clear()
                enemies_y.clear()
                for i in range(enemy_count):
                    enemies_x.append(randrange(0, width))
                    enemies_y.append(randrange(-100, 0))

        # Floor collision
        if ((player_y + p_height) >= floor_y):
            player_y -= 30









        # Game over condition




        # if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        #     car2_loc.center = right_lane, -200
        #     hearts = hearts - 1
        #     if(hearts == 0):
        #         break


        #Scoring
        for i in range(pumpkin_count):
            if(player_y >= (pumpkins_y[i] - 60) and player_y <= (pumpkins_y[i] + 60)):
                if(player_x >= (pumpkins_x[i] - 60) and player_x <= (pumpkins_x[i] + 60)):
                    score += 1
                    pumpkins_y[i] = -1000

        if(score == 15):
            print("YOU WON THE GAME!! 🎃🏆")
            main_menu()
            break;

        #Out
        for i in range(enemy_count):
            if(player_y >= (enemies_y[i] - 60) and player_y <= (enemies_y[i] + 60)):
                if(player_x >= (enemies_x[i] - 60) and player_x <= (enemies_x[i] + 60)):
                    hearts -= 1
                    enemies_y[i] = -1000


        # for i in range(enemy_count):

        if hearts <= 0:
            print("Game Over !!")
            main_menu()
            break;

        pygame.display.update()

    pygame.quit()
    