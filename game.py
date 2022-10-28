import pygame

def treasureHunt():
    pygame.init()
    win = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption("Treasure Hunt by aqeelshamz")
    bg = pygame.image.load("images/level1_bg.png")
    win.blit(bg, (0,0))

    x = 25
    y = 25

    width = 20
    height = 20

    speed = 2

    run = True

    while run:

        pygame.display.update()

    pygame.quit()

treasureHunt()