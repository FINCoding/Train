import pygame, sys
from pygame.locals import *
from math import floor
pygame.init()
screen = pygame.display.set_mode ((800,800),0,32)
pygame.display.set_caption("SHASHKI")
mainloop = True
# рисование клеток
x = 0
y = 0
c = 1
t = 1
col_b = (0,0,0)
col_w = (255,255,255)
A = [col_b, col_w]
B = [col_w, col_b]
D = []
 
oldhod = 0
while c <= 8:
    if c%2!= 0:
        D = A
    else:
        D = B
    while t <= 8:
        if t%2 != 0:
            i = 0
        else:
            i = 1
        rect_rect = Rect((x,y),(100,100))  
        rect_width = 0
        pygame.draw.rect(screen, D[i], rect_rect, rect_width)
        #рисование фишек
        if (c == 1 or c == 2 or c == 3) and D[i]==col_w:
            pygame.draw.circle(screen, (150, 200, 200), (x+50, y+50), 40)
        if (c == 6 or c == 7 or c == 8) and D[i]==col_w:
            pygame.draw.circle(screen, (255, 150, 5), (x+50, y+50), 40)    
        t = t + 1
        x = x + 100    
    y = y + 100    
    x = 0
    t = 1
    c = c + 1
###########
# выделение квадратика
col = col_w
def hod():
    global col, x, y, oldhod    
    if {oldhod} != 0:
        pygame.draw.rect(screen, col, Rect((x,y),(100,100)), 2)
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] <=100:
        x = 0
    elif (mouse_pos[0] > 100 and mouse_pos[0] <=200):
        x = 100
    elif (mouse_pos[0] > 200 and mouse_pos[0] <=300):
        x = 200
    elif (mouse_pos[0] > 300 and mouse_pos[0] <=400):
        x = 300
    elif (mouse_pos[0] > 400 and mouse_pos[0] <=500):
        x = 400
    elif (mouse_pos[0] > 500 and mouse_pos[0] <=600):
        x = 500
    elif (mouse_pos[0] > 600 and mouse_pos[0] <=700):
        x = 600
    elif (mouse_pos[0] > 700 and mouse_pos[0] <=800):
        x = 700    
    if mouse_pos[1] <=100:
        y = 0
    elif (mouse_pos[1] > 100 and mouse_pos[1] <=200):
        y = 100
    elif (mouse_pos[1] > 200 and mouse_pos[1] <=300):
        y = 200
    elif (mouse_pos[1] > 300 and mouse_pos[1] <=400):
        y = 300
    elif (mouse_pos[1] > 400 and mouse_pos[1] <=500):
        y = 400
    elif (mouse_pos[1] > 500 and mouse_pos[1] <=600):
        y = 500
    elif (mouse_pos[1] > 600 and mouse_pos[1] <=700):
        y = 600
    elif (mouse_pos[1] > 700 and mouse_pos[1] <=800):
        y = 700
    pygame.draw.rect(screen, (250,170,10), Rect((x,y),(100,100)), 2)
    k = floor (mouse_pos[0] / 100)
    l = floor (mouse_pos[1] / 100)
    if k%2 == 0:
        if l%2 != 0:
            col = col_w
        else:
            col = col_b
    else:
        if l%2 != 0:
            col = col_b
        else:
            col = col_w 
            
    pygame.display.update()
#################  
pygame.display.update()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            hod()

pygame.quit()
