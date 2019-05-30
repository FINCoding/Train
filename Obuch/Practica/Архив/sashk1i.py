import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode ((800,800),0,32)
pygame.display.set_caption("SHASHKI")
mainloop = True
# рисование клеток
x = 0
y = 0
c = 1
t = 1
A = [0, 2, 0, 2, 0, 2, 0, 2]
B = [2, 0, 2, 0, 2, 0, 2, 0]
D = []
while c <= 8:
    if c%2!= 0:
        D = A
    else:
        D = B
    #print (D)    
    i=0    
    while t <= 8:        
        rect_col = (255,255,255)
        rect_rect = Rect((x,y),(100,100))  
        rect_width = D[i]
        pygame.draw.rect(screen, rect_col, rect_rect, rect_width)
        t = t+1
        x = x + 100
        i = i + 1
    y = y + 100    
    x = 0
    t = 1
    c=c+1
    
pygame.display.update()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

pygame.quit()
