# pygame0.py
# Program to play with pygame.
# Kate May 2024

import pygame

# Initialize pygame
pygame.init()

# Create a pygame window
size = (600,400)
screen = pygame.display.set_mode(size)

# Display the window
pygame.display.flip()

# flip() is needed because drawing to the screen is the slowest
# step in animation. (Think back to your timing of your life programs).
# As a result most animation programs allow the programmer to state
# when the screen should be redrawn. Typically you draw a scene into
# window buffer in memory (which is fast) then call flip to copy that
# buffer to the screen. You will sometimes hear this referred to as
# double-buffering.
