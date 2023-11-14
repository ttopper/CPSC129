# pygame_test_4.py
# Tim Topper NCIT 212 Winter 2010
#
# If two are good more must be better.
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

radius = 20
for r in range(0, SCREEN_HEIGHT/radius):
    for c in range(0, SCREEN_WIDTH/radius):
        pygame.draw.circle(screen, TEAL,
                           ((2*c + 1)*radius, (2*r + 1)*radius),
                           radius, 1)
# The thing to notice here is the way we are calculating the locations for the
# centers of the circles. Try using c*radius and r*radius instead to see what
# happens.

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

