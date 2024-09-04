# pygame3.py
# Program to play with pygame.
# Kate May 2024

import pygame

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
size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption('Conway\'s Game of Life')

# Draw many shapes
radius = 20
for r in range(SCREEN_HEIGHT//radius):
    for c in range(SCREEN_WIDTH//radius):
        pygame.draw.circle(screen, TEAL,
                           ((2*c + 1)*radius, (2*r + 1)*radius), radius, 1)
# The thing to notice here is the way we are calculating the locations for the
# centers of the circles. Try using c*radius and r*radius instead to see what
# happens.

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

