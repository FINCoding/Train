from tkinter import *
from tkinter.filedialog import askopenfilename
win = Tk()
path = askopenfilename()
# img = PhotoImage(file='D:\Projects\Train\\1.gif')
img = PhotoImage(file=path)
Button(win, image=img).pack()
win.mainloop()