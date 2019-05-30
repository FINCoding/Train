import sys
import pygame
import random
from math import floor
from tkinter import *
from tkinter.filedialog import *
import fileinput

image_size = (800, 600)

def open():
     op = askopenfilename()
     
    # image = pygame.image.load(op)
     #image = pygame.transform.scale(image, (800, 600))
     #display = pygame.display.set_mode(image_size)
     #pygame.display.set_caption("Pyatnashki")
     #display.blit (image, (0, 0))
     #pygame.display.flip()

          
root = Tk()
m = Menu(root)
root.config(menu=m)
root.title('Pyatnashki')
root.geometry('800x600+300+225')
fm = Menu (m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...", command = open)


root.mainloop()
