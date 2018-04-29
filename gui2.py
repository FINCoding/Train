import sys
from tkinter import *

def quit():
    print('Hello, i must be going...')
    sys.exit()

widget = Button(None, text='Hello widget world!', command = quit)
widget.pack(expand = YES)
widget.mainloop()
