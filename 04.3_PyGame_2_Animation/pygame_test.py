# pygame_test.py
import pygame
import sys
pygame.init()
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
pygame.draw.circle(screen, YELLOW, (100,100), 50, 2)
pygame.display.flip()

radius = 20
for r in range(1, SCREEN_HEIGHT//radius):
    for c in range(1, SCREEN_WIDTH//radius):
        pygame.draw.circle(screen, SILVER, (c*radius, r*radius), radius, 1)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
