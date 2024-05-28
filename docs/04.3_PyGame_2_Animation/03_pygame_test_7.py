# pygame_test_7.py
# Could you make the movement more convincing?
# Tim Topper edited by Kate Chatfield-Reed May 2024
import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

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
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen.fill( BLACK )
x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2

pygame.draw.rect(screen, SILVER, (x, y, 5, 5))
pygame.display.flip()

for step in range(0, 75):
    # The key to animation is that you erase the old shape, and then
    # redraw it in its new slightly shifted position.
    # We erase by drawing a black copy of our shape over itself
    # (black since that is the colour of our background).
    pygame.draw.rect(screen, BLACK, (x, y, 5, 5))
    # If we had an image as our background, say of clouds, we'd have
    # to save the piece of it before we first draw a shape on it,
    # so we could place it back to erase our shape.
    x += 2
    y += 2
    pygame.draw.rect(screen, SILVER, (x, y, 5, 5))
    pygame.display.flip()
    pygame.time.delay(20)

running = True
while running:
    for event in pygame.event.get():
        # Handle the click
        if event.type == pygame.QUIT:
            running = False
    
# Close the window
pygame.quit()

