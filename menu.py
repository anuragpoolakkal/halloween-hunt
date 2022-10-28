import pygame
import button
import game
import os

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

pygame.init()

#create game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

bg_img = pygame.image.load(os.path.join("images", "bitlords_poster.png"))
screen.blit(bg_img, (0, 0))

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
start_img = pygame.image.load("images/button_start.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
start_button = button.Button(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 200, start_img, 1)
quit_button = button.Button((SCREEN_WIDTH / 2) - 65, SCREEN_HEIGHT / 2, quit_img, 1)


def main_menu():
  #game variables
  game_paused = True
  menu_state = "main"
  
  #game loop
  
  run = True
  while run:

    #check if game is paused
    if game_paused == True:
      #check menu state
      if menu_state == "main":
        #draw pause screen buttons
        if start_button.draw(screen):
          game_paused = False
        if quit_button.draw(screen):
          run = False
      #check if the options menu is open
      
    else:
      game.level1()

    #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          game_paused = True
      if event.type == pygame.QUIT:
        run = False

    pygame.display.update()

  pygame.quit()