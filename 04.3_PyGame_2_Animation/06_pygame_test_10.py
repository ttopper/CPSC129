# pygame_test_10.py
# How about a real ball?
# Tim Topper edited by Kate Chatfield-Reed May 2024
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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen.fill( BLACK )
pygame.display.flip()

# To bounce something more interesting than a rectangle we import
# a bitmap image to move around.
# Not much else changes.
ball = pygame.image.load("Aqua-Ball-icon.png")
ball_size = 16 # We'l see how to extract this from the bitmap later.

x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2
speed_x = 2
speed_y = 2
running = True
while running:
    # Note: ball_size replaces 5 here:
    pygame.draw.rect(screen, BLACK, (x, y, ball_size, ball_size))
    x += speed_x
    y += speed_y
    # here:
    if x+ball_size >= SCREEN_WIDTH or x <= 0:
        speed_x = -speed_x
    # and here:
    if y+ball_size >= SCREEN_HEIGHT or y <= 0:
        speed_y = -speed_y
    screen.blit(ball, (x, y))
    pygame.display.flip()
    pygame.time.delay(10) # Try 2 for arcade speed. Comment it out for max speed.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()

