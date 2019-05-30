from tkinter import *
import time
def button_clicked():
    print (u"Клик!")
    button['text']= time.strftime('%H:%M:%S')
root = Tk()
button = Button(root)
button.configure(text = time.strftime('%H:%M:%S'), command=button_clicked)
button.pack() 
button1 = Button (root, bg="red", text=u"Кликни меня!", command=button_clicked)
button1.pack()
root.mainloop()
