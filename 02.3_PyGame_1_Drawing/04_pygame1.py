# pygame1.py
# Program to play with pygame.
# Kate May 2024

import pygame

pygame.init()

size = (600,400)
screen = pygame.display.set_mode(size)

# Display the window with a snazzy caption
pygame.display.set_caption('Conway\'s Game of Life')

# Create a main loop
running = True
while running:
    # This is how pygame dectects user events, e.g. mouse movements
    # and clicks, keypresses, and window events like clicking the
    # x close icon.
    for event in pygame.event.get():
        # pygame.QUIT is the event fired by clicking the window close icon,
        # i.e. the x in the upper right corner of MS Windows windows.
        if event.type == pygame.QUIT:
            running = False

# Close the window
pygame.quit()
