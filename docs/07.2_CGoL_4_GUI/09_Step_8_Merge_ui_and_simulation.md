# Step 8: Merge the UI and the simulation code

The last step is to connect the menu to the actions. That is a job for 
the assignment, but we will do a little bit of planning to get you 
started. One important decision we need to figure out where to age the 
universe. The ageing happens inside the main event loop. The event loop 
will be divided into two parts one to handle events and the other to 
play the game of life. The ageing of the universe will have to respond 
to the game state which can be `PAUSE`, `STEP`, or `PLAY`.

```python
(PAUSE, STEP, PLAY) = list(range(3))

running = True
while running:
    # Handles events (if any):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x = event.pos[0]
            y = event.pos[1]
            print("mouse at ", (x,y))
            print(menu_area.inside(x,y)) 
            if menu_area.inside(x,y):
                menu_position = (x - menu_area.left)//GRID_SIZE
                print('Menu item: ', menu_position)
                if menu_position < len(menu):
                    menu[menu_position][0]()

    # Simulates the Game of Life:

    if game_state != PAUSE: 
        # Create the next universe:

        # Age the universe:

        # Replace the universe with next universe

        # Display the universe

    # if the game state is STEP it will age once and then switch state back to PAUSE
    # otherwise if the game state is PLAY it will stay PLAY and keep ageing the universe
    if game_state == STEP:
        game_state = PAUSE

pygame.quit()
```

Now let's think about what each of our functions has to do.

```python
#...............................................................................
# XXX Game Functions
#
def load():
    # Set state to PAUSE,
    # conduct a dialogue about what file to load,
    # and load it.
    #
    # What to do if the size of the universe in the file is not the same
    # as ours? If it is smaller? If it is larger?
    print('Running load') # For debugging.
    
def save():
    # Set state to PAUSE,
    # conduct a dialogue about what file to save to,
    # and save it.
    print('Running save') # For debugging.
    
def pause():
    # Set state to PAUSE.
    print('Running pause') # For debugging.
    
def step():
    # Set state to STEP.
    print('Running step') # For debugging.
    
def play():
    # Set state to PLAY.
    print('Running play') # For debugging.
    
def edit():
    # Set state to PAUSE.
    # Watch for mouse clicks in game region and kill and birth cells accordingly.
    #     Get mouse click coords.
    #     Convert to cell coords.
    #     Flip state of cell in universe AND onscreen.
    print('Running edit') # For debugging.
    
def clear():
    # Set state to PAUSE.
    # Clear the universe, i.e. make all cells dead.
    # Clear the screen.
    print('Running clear') # For debugging.
    
def null():
    print('Doing nothing') # For debugging.
    pass

# We also need to initialize our universe.

```

You can use the code in [life_gui_6.py](life_gui_6.py) as a starting 
point. Feel free to substitute your code in if you want to use a more 
recent (efficient) ageing algorithm.  