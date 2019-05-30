#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import fileinput
from tkinter.filedialog import *

image_size = (800, 600)
file = askopenfilename(filetypes=[("image files","*.jpg;*.png;*.bmp")])
print (file)
if file:
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, (800, 600))
    display = pygame.display.set_mode(image_size)
    pygame.display.set_caption("Pyatnashki")
    display.blit (image, (0, 0))
    pygame.display.flip()
