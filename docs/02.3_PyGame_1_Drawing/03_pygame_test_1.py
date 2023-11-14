# pygame_test_1.py
# Tim Topper NCIT 212 Winter 2010
#
# Is pygame working?
import pygame
import sys

# Initialize pygame.
pygame.init()

# Create a pygame display window.
screen = pygame.display.set_mode( (600, 400) )
# Paint the window black. (0, 0, 0) is an RGB colour triplet.
screen.fill( (0, 0, 0) )
# Display the changes we have made to the window.
pygame.display.flip()

# flip() is needed because drawing to the screen is the slowest
# step in animation. (Think back to your timing of your life programs).
# As a result most animation programs allow the programmer to state
# when the screen should be redrawn. Typically you draw a scene into
# window buffer in memory (which is fast) then call flip to copy that
# buffer to the screen. You will sometimes hear this referred to as
# double-buffering.

