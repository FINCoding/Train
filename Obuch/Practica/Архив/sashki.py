import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode ((800,800),0,32)
pygame.display.set_caption("SHASHKI")
mainloop = True
rect_1_col = (200,0,222)
rect_2_col = (0,0,255)
rect_1_rect = Rect((0,0),(100,100)) 
rect_2_rect = Rect((150,150),(100,100))
rect_1_width = 0 
rect_2_width = 4
x = 0
y = 0
c = 0
t = 0
while c < 8:
    while t < 8:        
        rect_col = (0,0,255)
        rect_rect = Rect((x,y),(100,100))
        if 
        rect_width = 4
        pygame.draw.rect(screen, rect_col, rect_rect, rect_width)
        t = t+1
        x = x + 100
    y = y + 100    
    x = 0
    t=0
    c=c+1
#pygame.draw.rect(screen, rect_1_col, rect_1_rect, rect_1_width) 
#pygame.draw.rect(screen, rect_2_col, rect_2_rect, rect_2_width)
pygame.display.update()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

pygame.quit()
