# pygame_test_3.py
# Tim Topper NCIT 212 Winter 2010
#
# Plain black is boring.
import pygame
import sys

# (0, 128, 128) is a mysterious triplet so we'll follow our previous practice
# of replacing magic literals with symbolic names.
# Here are some common colours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

pygame.init()

# We'll replace the 600 and 400 with symbolic names too.
# This also let's us use them for screen-aware calculations, e.g. line 31.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

screen.fill( BLACK )
pygame.draw.circle(screen, YELLOW, (100,100), 50, 2)
pygame.draw.circle(screen, TEAL, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 50, 1)
# As you typed the ( after circle above you should have noticed IDLE prompting
# you for the arguments. Their names let you know what the arguments mean.
# If that hint is insufficient you can use help(pygame.draw.circle) in the
# Python shell to get more information.
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

