# pygame_test_5.py
# Tim Topper NCIT 212 Winter 2010
#
# What else can we draw?
#
# For more shapes try dir(pygame.draw) in the shell window.
#
# In addition to drawing shapes pygame lets you draw bitmapped text (i.e. real fonts)
# to the screen, and to manipulate images a the pixel level.
import pygame
import sys

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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen.fill( BLACK )

pygame.draw.rect(screen, GREY, (200, 100, 300, 200))
pygame.draw.circle(screen, YELLOW, (500,300), 50, 2)
pygame.draw.polygon(screen, RED, ((20,20), (50,120),
                                  (0, SCREEN_HEIGHT),
                                  (SCREEN_WIDTH/2, 0)) )
pygame.draw.line(screen, WHITE, (200,100), (500,300), 4)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

