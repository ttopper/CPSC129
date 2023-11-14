# pygame_test_2.py
# Tim Topper NCIT 212 Winter 2010
#
# Exiting gracefully.
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (600, 400) )
screen.fill( (0, 0, 0) )
pygame.display.flip()

# The main event loop.
while True:
    # This is how pygame dectects user events, e.g. mouse movements
    # and clicks, keypresses, and window events like clicking the
    # x close icon.
    for event in pygame.event.get():
        # pygame.QUIT is the event fired by clicking the window close icon,
        # i.e. the x in the upper right corner of MS Windows windows.
        if event.type == pygame.QUIT:
            # Close down pygame.
            pygame.quit()
            # Exit this instance of the Python interpreter.
            # This will generate a traceback in the shell window,
            # but that traceback is not reporting errors.
            sys.exit()
