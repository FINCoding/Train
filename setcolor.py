from tkinter import *
from tkinter.colorchooser import askcolor

def setBgColor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)

def titleScr():
    str = input('Input title for Screnn...')
    root.title(str)

root = Tk()
push = Button(root, text='Set Background Color', command=setBgColor)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(side=LEFT, fill=BOTH)
push2 = Button(root, text='Change scr title', command=titleScr)
push2.pack(side=RIGHT, fill=BOTH)
root.mainloop()