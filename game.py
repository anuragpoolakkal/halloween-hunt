import pygame
import os

# shape parameters
size = width, height = (1200, 800)


pygame.init()
win = pygame.display.set_mode(size)
bg_img = pygame.image.load(os.path.join("images", "level1_bg.png"))
bg = pygame.transform.scale(bg_img, (1200, 800))

#width = 1200

i = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    # Create looping background
    win.blit(bg, (0, 0))

    pygame.display.update()

    # load player vehicle
    ground_floor = pygame.image.load(os.path.join("images", "level1_land.png"))
    # resize image
    #car = pygame.transform.scale(car, (250, 250))
    car_loc = ground_floor.get_rect()
    car_loc.center = width/2, height*0.8
    pygame.display.update()

pygame.quit()
