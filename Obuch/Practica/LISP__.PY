from random import randrange as rnd, choice 
from tkinter import * 
root = Tk() 
root.geometry('800x600') 
canv = Canvas(root, bg = 'white') 
canv.pack(fill = BOTH, expand = 10) 
colors = ['red','brown','green','lightgreen','yellow','black','blue'] 
def fill_random(event): 
    global balls 
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
        
def line_on(event):
    canv.bind('<Button-3>', line_off)
    canv.bind('<Motion>', task)

def line_off(event):
    canv.bind('<Button-3>', line_on)
    canv.unbind('<Motion>')

def task(event):
    canv.delete('lines')
    x = event.x
    y = event.y
    for b in balls:
        canv.create_line(x,y,b.x,b.y, fill = 'orange', width = 2, tag = 'lines')
    #balls[-1].kill()
       
    pass 

fill_random(0) 
canv.bind('<Button-1>', fill_random) 
canv.bind('<Button-3>', line_on) 

mainloop() 
