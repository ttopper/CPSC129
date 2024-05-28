# pygame_test_8.py
# Will it crash?
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
pygame.draw.rect(screen, SILVER, (x, y, 5, 5))
pygame.display.flip()

# 75 steps wasn't enough for our shape to get to the wall.
# Try increasing the number of steps in pygame_test_7 to see what happens
# when it gets to the wall.

# Now let's make it bounce.
# To bounce we will need to change it's direction of travel,
# which means that instead of always adding 2 to its x and y coordinates
# we will sometimes need to subtract 2 from one or both.
# Since the speed in each direction will change we will make it a variable:
speed_x = 2 # Initial horizontal speed.
speed_y = 2 # Initial vertical speed.
for step in range(0,500):
    pygame.draw.rect(screen, BLACK, (x, y, 5, 5))
    x += speed_x
    y += speed_y
    # If our x coordinate reaches the far right hand side (RHS) of the screen
    # we need to bounce off that wall.
    # Why the +5? It accounts for the fact that our rectangle's position is
    # given by the coordinates of its upper-left corner. Since our rectangle
    # is 5 pixels wide, we reach the RHS when its x position is still 5 pixels
    # from the wall.
    if x+5 >= SCREEN_WIDTH:
        #  We bounce horizontally by reversing our x speed.
        speed_x = -speed_x
    # Same for y...
    if y+5 >= SCREEN_HEIGHT:
        speed_y = -speed_y
    pygame.draw.rect(screen, YELLOW, (x, y, 5, 5))
    pygame.display.flip()
    pygame.time.delay(20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

