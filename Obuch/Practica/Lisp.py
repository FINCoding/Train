from random import randrange as rnd 
from tkinter import * 
scr = Tk() 
scr.geometry('400x400')
fr = Frame(scr)
fr.pack(fill = X, pady = 5)
bt1 = Button(fr, width = 8, text = 'Пыщь')
bt1.pack(side = 'left', padx = 2)
bt2 = Button(fr, width = 8, text = 'increase')
bt2.pack()
bt3 = Button(fr, width = 8, text = 'delete')
bt3.pack()
canv = Canvas(scr, bg = 'white') 
canv.pack(fill = BOTH, expand = 1)
colors = ['red','brown','green','lightgreen','yellow','black','blue']
class ball():
    def __init__(self):
        x = self.x = rnd(100,300)
        y = self.y = rnd(100,300)
        r = self.r = rnd(10,30)
        self.width = rnd(0,5)
        self.color = colors[rnd(0,5)]
        self.pen_color = colors[rnd(0,5)]
        self.id = canv.create_oval(x-r, y-r, x+r, y+r, width = self.width, fill = self.color,
                                   outline = self.pen_color)
        
    def paint(self):
        x = self.x 
        y = self.y 
        r = self.r 
        canv.coords(self.id,x-r,y-r,x+r,y+r)
        canv.itemconfig (self.id, width = self.width, fill = self.color, outline = self.pen_color)

    
    def kill(self):
        global balls
        id = len(balls)
        print(id)
        canv.delete(self.id) 
        balls.remove(self)

def remove(event):
    global balls
    l = len(balls)
    b = balls[l-1]
    b.kill()
    

def align_x():
    global balls
    x = 30
    y = 0
    for b in balls:
        b.y = 200
        #setattr(b, 'y', 200)
        #setattr(b, 'x', x)
        b.x = x
        x += 60
        b.r = getattr(b, 'r') 
        b.paint()
        scr.geometry(str(x) + 'x' + str(b.y+200))
def fill_random(event):
    global balls
    canv.delete(ALL)
    balls = []
    for z in range(12):
        balls += [ball()]
    align_x()
def increase_red(event):
    global balls
    for b in balls:
        a = getattr(b, 'color')
        r = getattr(b, 'r')
        if a == 'red':
            b.r = b.r * 2.5
            #setattr(b, 'r', nr) 
            b.paint()
        
    

bt1.bind('<Button-1>',fill_random)
bt2.bind('<Button-1>', increase_red)
bt3.bind('<Button-1>', remove)

mainloop()

