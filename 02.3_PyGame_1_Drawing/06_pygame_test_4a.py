# pygame_test.py
import pygame
import sys
pygame.init()

u_size = (25, 80)

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

screen.fill(BLACK)
pygame.display.flip()

size = 20
for r in range(0, SCREEN_HEIGHT//size):
    pygame.draw.line(screen, SILVER, (0, r*size), (SCREEN_WIDTH, r*size))
for c in range(0, SCREEN_WIDTH//size):
    pygame.draw.line(screen, SILVER, (c*size, 0), (c*size, SCREEN_WIDTH))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
