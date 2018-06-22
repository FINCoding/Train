from Useful.launchmodes import PortableLauncher
demoModules = ['demoCheck', 'demoRadio','demoScale']

for demo in demoModules:
    PortableLauncher(demo, demo + '.py')()

# root = Tk()
# root.title('Processes')
# Label(root, text='Multiple program demo: command lines', bg='white').pack()
# root.mainloop()