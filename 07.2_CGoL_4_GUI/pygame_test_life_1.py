# pygame_test_life_1.py
import pygame
import sys
import time
import random
pygame.init()

u_size = (25, 40)

cell = pygame.image.load("Aqua-Ball-icon.png")
cell_size = 16
grid_size = cell_size + 1

SCREEN_HEIGHT = u_size[0]*grid_size + 1
SCREEN_WIDTH = u_size[1]*grid_size + 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def load(): pass
def save(): pass
def pause(): pass
def step(): pass
def simulate(): pass
def edit(): pass
def clear(): pass


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

screen.fill(BLACK)
pygame.display.flip()

# Display menu.
MENU_HEIGHT = 16
menu = [[load, "folder.png"], [save, "folder_add.png"],
        [None, "black_separator.png"],
        [pause, "control_pause_blue.png"], [step, "control_play_blue.png"],
        [simulate, "control_fastforward_blue.png"],
        [None, "black_separator.png"],
        [edit, "pencil.png"], [clear, "picture_empty.png"]
        ]

for i in range(len(menu)):
    menu[i].append(pygame.image.load(menu[i][1]))
    screen.blit(menu[i][2], (i*grid_size + 1, 0))
    
# Draw horizontal lines.
for r in range(0, SCREEN_HEIGHT/grid_size):
    pygame.draw.line(screen, GREY, (0, r*grid_size), (SCREEN_WIDTH, r*grid_size))
# Draw vertical lines.
for c in range(0, SCREEN_WIDTH/grid_size):
    pygame.draw.line(screen, GREY, (c*grid_size, MENU_HEIGHT+1), (c*grid_size, SCREEN_WIDTH))
#pygame.display.flip()

time.sleep(1)
for i in range(1,100):
    screen.blit(cell, (random.randint(1, u_size[1])*grid_size+1, random.randint(1, u_size[0])*grid_size+1))
    #time.sleep(0.2)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
