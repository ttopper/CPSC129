# pygame_test_9.py
# All four walls and forever.
# BUG: Not bouncing quite right off top and left. (Look carefully).
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

x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2
speed_x = 2
speed_y = 2

# To bounce forever we move our movement code into the main event loop --
# straight copy and paste.
running = True
while running:
    pygame.draw.rect(screen, BLACK, (x, y, 5, 5))
    x += speed_x
    y += speed_y
    # To get it to bounce off all four walls, we add tests to check if we
    # have reached the top or left walls as well as the right and bottom walls.
    if x+5 >= SCREEN_WIDTH or x-5 <= 0:
        speed_x = -speed_x
    if y+5 >= SCREEN_HEIGHT or y-5 <= 0:
        speed_y = -speed_y
    # It doesn't bounce quite right off the top and left walls though.
    # Can you spot the problem?
    # Hint: Check the calculations of position carefully.
    pygame.draw.rect(screen, YELLOW, (x, y, 5, 5))
    pygame.display.flip()
    pygame.time.delay(10) # Try 2 for arcade speed. Comment it out for max speed.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()

