import pygame, sys

window = pygame.display.set_mode((800,800), 0, 32)
pygame.display.set_caption("SHASHKI")

screen = pygame.Surface((800,800))

class board:
    def __init__(self):
        pass
    def rectangle(self):
        pass
class shashki:
    count = 8

    def __init__(self, color):
        self.color = color
    def step(self):
        pass
    #def distinguish(self):            
          
                           
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            pass            
    window.blit(screen, (0,0))
    pygame.display.flip()

