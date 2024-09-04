# Step 5: Refactoring interlude

The calculations for the positions of the grid and the cells are 
starting to get a bit long and complicated. Before we move forward it 
would be nice to clean up the code a little by replacing some of those 
calculations with variables. We will want variable names for the grid, 
and probably the menu area when we start working with that. Both the 
grid and the menu area are rectangular regions on the screen. We will 
encapsulate with a class that can handle rectangluar regions in our 
screen. We are going to define our rectangular region with a pair of 
coordinates, one pair at the top left and one pair at the bottom right. 

```python
class Rectangle:
    '''             |      |
                    | top  |
                    |      | bottom
        +--------+  -      |
        |        |         |
        +--------+         -

--------| left
-----------------| right

    '''
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
```

The first rectangle we are going to define is a game area.

```python
game_area = Rectangle(BORDER_WIDTH + MENU_HEIGHT, BORDER_WIDTH,
                      SCREEN_HEIGHT - BORDER_WIDTH - 1, 
                      SCREEN_WIDTH - BORDER_WIDTH - 1)

# We can now use the rectangle object to easily find the placement of the grid
# Draw horizontal lines.
for y in range(0, U_ROWS+1):
    pygame.draw.line(screen, GREY, (game_area.left, game_area.top + y*grid_size),
                     (game_area.right, game_area.top + y*grid_size))

# Draw vertical lines.
for x in range(0, U_COLS+1):
    pygame.draw.line(screen, GREY, (game_area.left + x*grid_size, game_area.top ),
                     (game_area.left + x*grid_size, game_area.bottom))
pygame.display.flip()

# We can also use the Rectangle to place the cells
for i in range(1,100):
    # + 1s below move past LH borderline, below upper borderline.
    screen.blit(live_cell, (game_area.left + random.randint(0, U_COLS-1)*grid_size+1,
                            game_area.top + random.randint(0, U_ROWS-1)*grid_size+1))
pygame.display.flip()

```

This makes our code easier to read because we can see that we are 
working from very clear reference points in our game area. Now we are 
ready to start working on the menu.