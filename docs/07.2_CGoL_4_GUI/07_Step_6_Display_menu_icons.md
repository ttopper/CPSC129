# Step 6: Display the menu icons

The next job is to display the menu icons. We are going to need to get 
the icons, load them, and blip them to our screen in the right location. 
The locations will all be in our menu area. Let's start by defining a 
Rectangle for our menu area.

```python
MENU_HEIGHT = 16
SCREEN_BORDER = 10
SCREEN_HEIGHT = U_ROWS*GRID_SIZE + 1 + 2*SCREEN_BORDER + MENU_HEIGHT # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*GRID_SIZE + 1 + 2*SCREEN_BORDER

menu_area = Rectangle(BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH + MENU_HEIGHT,
                      SCREEN_WIDTH - BORDER_WIDTH)
```

The next thing we need to do is load our graphics. We've done that once 
before when we loaded our Aqua-Ball. Let's look at that code.

```python
live_cell = pygame.image.load("Aqua-Ball-icon.png")
```

We need to do that same thing for all of our menu icons (load, save, 
pause, step, play, edit, clear). You can download all of the appropriate 
images [here](01_The_goal.md). Loading the images will look like this:


```python
load_icon = pygame.image.load("folder.png")
save_icon = pygame.image.load("folder_add.png")
pause_icon = pygame.image.load("control_pause_blue.png")
step_icon = pygame.image.load("control_play_blue.png")
play_icon = pygame.image.load("control_fastforward_blue.png")
edit_icon = pygame.image.load("pencil.png")
clear_icon = pygame.image.load("picture_empty.png")
```

I used `_icon` as part of the names, because the variable names also 
sound like they would make good function names. The next step is to 
display all the images on the screen, but it really feels we should be 
able to simplify that process. We don't want to call blit 7 times, we 
would rather use a list to simplify the process. Rather than refactoring 
later, let's do some planning now. We will create a menu, which will be 
a list. Inside the list will be sublists that contain matching function 
names and file names. We will also include some blank separators between 
the different sections of our menu. To get the code working we will 
include some functions to go with each action. We aren't going to fill 
them in in.

```python

def load(): print('Running load')
def save():  print('Running save')
def pause():  print('Running pause')
def step():  print('Running step')
def play():  print('Running play')
def edit():  print('Running edit')
def clear():  print('Running clear')
def null(): print('Doing nothing')

menu = [ [load, "folder.png"], [save, "folder_add.png"],
         [null, "black_separator.png"],
         [pause, "control_pause_blue.png"], [step, "control_play_blue.png"],
         [play, "control_fastforward_blue.png"],
         [null, "black_separator.png"],
         [edit, "pencil.png"],  [clear, "picture_empty.png"]
         ]
```

The next step is to draw the menu. Now that all of our menu information 
is in a list, it should be relatively easy to draw it with a for loop. 
The loop will have to calculate where to put each item and were going to 
do that by multiplying the index by the `grid_size`, which means we're 
going to need to use `range`. As we load each image we will append it to 
the end of the corresponding menu items list.

```python
for i in range(len(menu)):
    # load and save the image in pygame
    menu[i].append(pygame.image.load(menu[i][1]))
    # display icon at position defined by the menu_area
    screen.blit(menu[i][2], (menu_area.left + i*grid_size + 1, menu_area.top)) # + 1 for border
```

This draws some beautiful icons.

![.](pygame_test_life_1.output.png){width="687" height="451"}
