from tkinter import *
def window_deleted():
    print ('Окно закрыто')
    root.quit() # явное указание на выход из программы
    pass (root)
root=Tk()
root.title('Пример приложения')
root.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
root.resizable(True, False) # размер окна может быть изменён только по горизонтали
root.mainloop()
