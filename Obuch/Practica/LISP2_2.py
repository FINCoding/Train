from random import randrange as rnd, choice
from tkinter import *
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg ='white')
canv.pack(fill = BOTH, expand = 1)
m = 34
d = 2
nr = 6
nc = 8
x0 = m//2
y0 = m//2
colors = ['red', 'yellow', 'green']
class cell():
    def __init__(self, r, c):
        self.n = rnd(10)
        self.color = choice(colors)
    def paint(self, r, c):
        x1 = x0 + c*m + d
        y1 = y0 + r*m + d
        x2 = x1 + m - 2*d
        y2 = y1 + m - 2*d
        canv.coords(self.id,x1,y1,x2,y2)
        canv.itemconfig(self.id, fill = self.color)
        x = (x1 + x2)/2
        y = (y1 + y2)/2        
        canv.coords(self.id_text,x,y) 
        canv.itemconfig(self.id_text, text = self.n) 

a = []

mainloop()
