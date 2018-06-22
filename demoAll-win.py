from tkinter import *
demoModules = ['demoCheck', 'demoRadio','demoScale']

def makePopus(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)
        window = Toplevel()
        demo = module.Demo(window)
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects

def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()

root = Tk()
root.title('Popups')
demos = makePopus(demoModules)
Label(root, text='Multiple Tolevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()
