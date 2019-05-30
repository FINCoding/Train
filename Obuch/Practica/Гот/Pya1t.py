import sys
import pygame
import random
from math import floor


image_file = "1.jpg"
image_size = (800, 600)
tile_width = 400
tile_height = 300
COLUMNS = 2
ROWS = 2
EMPTY_TILE = (COLUMNS-1, ROWS-1)

BLACK = (0, 0, 0)

hor_border = pygame.Surface((tile_width, 1))
hor_border.fill(BLACK)
ver_border = pygame.Surface((1, tile_height))
ver_border.fill(BLACK)

image = pygame.image.load(image_file)
image = pygame.transform.scale(image, (800, 600))
tiles = {}

for c in range(COLUMNS):
    for r in range (ROWS):
        tile = image.subsurface (
            c*tile_width, r*tile_height,
            tile_width, tile_height)
        tiles[(c, r)] = tile
        if (c, r)!=EMPTY_TILE:
            tile.blit(hor_border, (0, 0))
            tile.blit(hor_border, (0, tile_height-1))
            tile.blit(ver_border, (0, 0))
            tile.blit(ver_border, (tile_width-1, 0))
            tile.set_at((1, 1), BLACK)
            tile.set_at((1, tile_height-2), BLACK)
            tile.set_at((tile_width-2, 1), BLACK)
            tile.set_at((tile_width-2, tile_height-2), BLACK)            
tiles[EMPTY_TILE].fill(BLACK)

state = {(col, row):(col, row)
         for col in range(COLUMNS) for row in range(ROWS)}
(emptyc, emptyr) = EMPTY_TILE
pygame.init()
display = pygame.display.set_mode(image_size)
pygame.display.set_caption("Pyatnashki")
display.blit (image, (0, 0))
pygame.display.flip()

def shift (c, r) : 
    global emptyc, emptyr  
    display.blit(
        tiles[state[(c, r)]], 
        (emptyc*tile_width, emptyr*tile_height)) 
    display.blit(
        tiles[EMPTY_TILE],
        (c*tile_width, r*tile_height))
    state[(emptyc, emptyr)] = state[(c, r)]
    state[(c, r)] = EMPTY_TILE
    (emptyc, emptyr) = (c, r)
    pygame.display.flip() 

 
def shuffle() :
    global emptyc, emptyr
    # keep track of last shuffling direction to avoid "undo" shuffle moves
    last_r = 0
    for i in range(75):
        # slow down shuffling for visual effect
        pygame.time.delay(50)
        while True:
            # pick a random direction and make a shuffling move
            # if that is possible in that direction
            r = random.randint(1, 4)
            if (last_r + r == 5):
                # don't undo the last shuffling move 
                continue
            if r == 1 and (emptyc > 0):
                shift(emptyc - 1, emptyr) # shift left
                
            elif r == 4 and (emptyc < COLUMNS - 1):
                shift(emptyc + 1, emptyr) # shift right
                
            elif r == 2 and (emptyr > 0):
                shift(emptyc, emptyr - 1) # shift up
                
            elif r == 3 and (emptyr < ROWS - 1):
                shift(emptyc, emptyr + 1) # shift down
                
            else:
                # the random shuffle move didn't fit in that direction   
                continue 
            last_r=r 
            break # a shuffling move was made
def prov():
    b = 1
    for col in range(COLUMNS) :
        for row in range(ROWS) :
            if col != state[(col, row)][0] or row != state[(col,row)][1]:
                b = 0
                break;
    
    print (b)
    return b

 
# process mouse clicks  
at_start = True 
showing_solution = False 
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN :
        if at_start:
            # shuffle after the first mouse click
            shuffle()
            at_start = False
        elif event.dict['button'] == 1:
            # mouse left button: move if next to the empty tile
            mouse_pos = pygame.mouse.get_pos()
            c = floor (mouse_pos[0] / tile_width)
            r = floor (mouse_pos[1] / tile_height)
            print (c, r, emptyc, emptyr)
            if (    (abs(c-emptyc) == 1 and r == emptyr) or   
                    (abs(r-emptyr) == 1 and c == emptyc)):
                
                shift (c, r)
                if prov() == 1:
                    sys.exit()                
        elif event.dict['button'] == 3:
            # mouse right button: show solution image
            saved_image = display.copy()
            display.blit(image, (0, 0))
            pygame.display.flip()
            showing_solution = True 
    elif showing_solution and (event.type == pygame.MOUSEBUTTONUP):
        # stop showing the solution
        display.blit (saved_image, (0, 0))
        pygame.display.flip()
        showing_solution = False 

 


