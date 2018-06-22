from tkinter import *
from guiStreams import redirectedGuiShellCmd

def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='Go!', command=launch).pack()
window.mainloop()