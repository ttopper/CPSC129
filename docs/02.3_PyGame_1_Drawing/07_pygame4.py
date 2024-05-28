# pygame4.py
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
#pygame.display.set_caption('Conway\'s Game of Life')

# Draw some new shapes
pygame.draw.rect(screen, GREY, (200, 100, 300, 200))
pygame.draw.circle(screen, YELLOW, (500, 300), 50, 2)
pygame.draw.polygon(screen, RED, [[20, 20], [50, 120],
                                  [0, SCREEN_HEIGHT], [SCREEN_WIDTH//2, 0]])
pygame.draw.line(screen, WHITE, (200, 100), (500, 300), 4)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

