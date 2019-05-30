from random import randrange as rnd, choice 
from tkinter import * 
root = Tk() 
root.geometry('800x600') 
canv = Canvas(root, bg = 'white') 
canv.pack(fill = BOTH, expand = 10) 
colors = ['red','brown','green','lightgreen','yellow','black','blue']
balls = []
def fill_random(event): 
    global balls, A
    canv.delete(ALL) 
    balls = [] 
    for z in range(12): 
        balls += [ball()]


def paint(): 
    for b in balls: 
        b.paint()  

class ball(): 
    def __init__(self):
        x = self.x = rnd(50,700) 
        y = self.y = rnd(50,550) 
        r = self.r = rnd(10,30) 
        self.color = choice(colors) 
        self.pen_color = choice(colors) 
        self.width = 0 
        self.id = canv.create_oval(x-r,y-r,x+r,y+r, width = self.width, fill = self.color, outline = self.pen_color ) 
        self.paint()
    def paint(self): 
        x = self.x 
        y = self.y 
        r = self.r 
        canv.coords(self.id,x-r,y-r,x+r,y+r) 
        canv.itemconfig (self.id, fill = self.color, width = self.width, outline = self.pen_color) 
    def kill(self): 
        canv.delete(self.id) 
        balls.remove(self)
        
def task(event):
    global balls 
    x = event.x
    y = event.y
    bm = balls[0]    
    for b in balls[1:]:
        if ((b.x-x)**2 + (b.y - y )**2)<((bm.x - x)**2 + (bm.y - y)**2):
            bm = b
        bm.x += (bm.x - x)/12
        if bm.x < 0:
            bm.x += 80
        elif bm.x > 800:
            bm.x -= 80
        bm.y ++ (bm.y - y)/12
        bm.paint()

canv.bind('<Button-1>', fill_random)
canv.bind('<Motion>', task) 

mainloop()

