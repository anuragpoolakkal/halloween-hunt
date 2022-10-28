import pygame
import os

x = 1200
y = 800

pygame.init()
win = pygame.display.set_mode((1000, 500))
imp = pygame.image.load(os.path.join("images", "halloween_bkgrnd.jpg"))
bg_img = pygame.image.load(os.path.join("images","floor.png"))
bg = pygame.transform.scale(bg_img, (1000, 500))

DEFAULT_IMAGE_POSITION = (200,200)


width = 1000
i = 0

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    #Create looping background
    win.blit(imp, (0, 420))
    win.blit(bg, (i, 420))
    win.blit(bg, (width+i, 420))
    if i == -width:
        win.blit(bg, (width+i, 420))
        i = 0
    i -= 1

    pygame.display.update()