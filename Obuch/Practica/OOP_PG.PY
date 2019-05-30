import pygame
pygame.init()
window = pygame.display.set_mode ((800,800),0,32)
pygame.display.set_caption("SHASHKI")
screen = pygame.Surface((800,800))
mainloop = True
color = (255, 50, 0)
x = 0
y = 0
go_right = True
go_left = False

class circle:
    def __init__(self):
        pass
    def draw (self, color, x, y):
        pygame.draw.circle(screen, color, (x, y), 40)
c = circle()
z = circle()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
            pygame.quit()
    #if x > 800:
                
    a = c.draw(color, x, y)
    b = z.draw((10,100,50), x, y+50)
    x += 0.31     
    window.blit(screen, (100,100))
    pygame.display.flip()
        
