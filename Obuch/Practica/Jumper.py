from tkinter import*
import time
scr = Tk()
scr.geometry('800x600')
canv = Canvas(scr, bg='white')
canv.pack(fill=BOTH, expand=1)
def click(event):
    global j
    j.vx = (j.x - event.x)/10
    j.vy = (j.y - event.y)/10 

canv.bind('<Button-1>', click)

class Jumper(): 
    x = 40 
    y = 150 
    r = 20 
    id = canv.create_oval(x-r,y-r,x+r,y+r) 
    vy = 0 
    vx = 6    
    def move(self): # self - ссылка на себя 
        self.vy += 0.3 # свою скорость увеличить на 1,5 
        self.y += self.vy # к своей координате y прибавить свою скорость
        self.x += self.vx 
        self.vx *= 0.99 
        if self.y > 550 or self.y < 0: 
            self.vy *= -0.9 
        if self.x > 800 or self.x < 0:
            self.vx *= -0.9
        #if self.y in range(575,590):
            
        canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r) 

j = Jumper()    
while 1: # вечный цикл 
    j.move()
    canv.update() 
    time.sleep(0.03) 
mainloop()
