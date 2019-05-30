import sys
import pygame
import random
from tkinter import *
from tkinter.filedialog import *

def open():
     op = askopenfilename()

          
root = Tk()
m = Menu(root)
root.config(menu=m)
fm = Menu (m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...", command = open)

root.mainloop()
