# pygame_test_6.py
# Tim Topper NCIT 212 Winter 2010
#
# Enough with the art, make something move.
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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen.fill( BLACK )

# Starting x and y coordinates for our shape.
x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT/2

pygame.draw.rect(screen, SILVER, (x, y, 5, 5))
pygame.display.flip()

for step in range(0,50):
    # Move the shape by changing the x and y coordinates.
    x += 2
    y += 2
    pygame.draw.rect(screen, SILVER, (x, y, 5, 5))
    pygame.display.flip()
    # Assign the speed at which we want things to happen.
    pygame.time.delay(20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

