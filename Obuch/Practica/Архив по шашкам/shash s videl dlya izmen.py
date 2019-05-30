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
c = 0
t = 0
col_y = (255, 150, 5)
col_bl = (150, 200, 200)
col_w = (255,255,255)
col_b = (0,0,0)
color_rect = []
tiles1 = {}
tiles2 = {}
kbel = {}
oldhod = 0 
itb = 0
ity = 0
ok = 900
ol = 900
sk = 0
sl = 0
nk = 0
nl = 0
vibrano = ''
while c < 8:
    if c%2 == 0:
        color_rect = [(0,0,0), (255,255,255)]
    else:
        color_rect = [(255,255,255), (0,0,0)]
    while t <= 7:
        if t%2 == 0:
            i = 0
        else:
            i = 1            
        rect_rect = Rect((x,y),(100,100))  
        rect_width = 0
        pygame.draw.rect(screen, color_rect[i], rect_rect, rect_width)
        if color_rect[i] == (0,0,0):
            kbel[(t, c)] = 'Black'  
        #рисование фишек
        if (c == 0 or c == 1 or c == 2) and color_rect[i]==(255,255,255):
            pygame.draw.circle(screen, col_bl, (x+50, y+50), 40)
            tiles1[(t, c)] = itb
            itb = itb + 1
        if (c == 5 or c == 6 or c == 7) and color_rect[i]==(255,255,255):
            pygame.draw.circle(screen, col_y, (x+50, y+50), 40)
            tiles2[(t, c)] = ity
            ity = ity + 1          
        t = t + 1
        x = x + 100
    y = y + 100    
    x = 0
    t = 0
    c = c + 1
###########
# выделение квадратика
color = (255,255,255)
def videl():
    global color, x, y, oldhod  
    if {oldhod} != 0:
        pygame.draw.rect(screen, color, Rect((x,y),(100,100)), 4)
    mouse_pos = pygame.mouse.get_pos()
    k = floor (mouse_pos[0] / 100)
    l = floor (mouse_pos[1] / 100)
    x = k*100
    y = l*100 
    pygame.draw.rect(screen, (0,170,0), Rect((x,y),(100,100)), 4)    
    if k%2 == 0:
        if l%2 != 0:
            color = (255,255,255)
        else:
            color = (0,0,0)
    else:
        if l%2 != 0:
            color = (0,0,0)
        else:
            color = (255,255,255)
    pygame.display.update()
    
def hod():
    global vibrano, sk, sl
    mouse_pos = pygame.mouse.get_pos()
    sk = floor (mouse_pos[0] / 100)
    sl = floor (mouse_pos[1] / 100)
    if (sk, sl) in tiles1:
        vibrano = 'B'
    if (sk, sl) in tiles2:
        vibrano = 'Y'
    if (sk, sl) in kbel:
        vibrano = 'Nelzya'
def smena_pol():
    global nk, nl
    if vibrano == 'Y':
        if ok != 900:
            pygame.draw.circle(screen, (255, 255, 255), (ok*100+50, ol*100+50), 40)
            ity = tiles2[(ok,ol)]
            del tiles2[(ok, ol)]
    elif vibrano == 'B':
        if ok != 900:
            pygame.draw.circle(screen, (255, 255, 255), (ok*100+50, ol*100+50), 40)
            itb = tiles1[(ok,ol)]
            del tiles1[(ok, ol)]
    mouse_pos = pygame.mouse.get_pos()        
    nk = floor (mouse_pos[0] / 100)
    nl = floor (mouse_pos[1] / 100)
    x = nk*100+50
    y = nl*100+50    
    if vibrano == 'Y':
        pygame.draw.circle(screen, col_y, (x,y), 40)
        if ok != 900:
            tiles2[(nk,nl)] = ity
    elif vibrano == 'B':
        pygame.draw.circle(screen, col_bl, (x,y), 40)
        if ok != 900:
            tiles1[(nk,nl)] = itb       
    pygame.display.update()    
    
#################  
pygame.display.update()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False            
        if event.type == pygame.MOUSEBUTTONDOWN :
            videl()
            hod()
            if vibrano in ('B', 'Y'):
               smena_pol()
               ok = sk
               ol = sl
            else:
               ok = 900        
pygame.quit()
