from tkinter import *
root = Tk()

def doit():
    i = int(scl.get())
    scl2.set(i)
scl = Scale(root, from_=0, to=10, tickinterval=1)
scl2 = Scale(root, from_=0, to=10, tickinterval=1, orient='horizontal')
scl2.pack(expand=YES, fill=X)
scl.pack(side=TOP, expand=YES, fill=Y)

root.mainloop()
