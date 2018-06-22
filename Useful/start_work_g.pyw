from tkinter import *
from quitter import Quitter
import os, sys

class startWork(Frame):
    demos = {
        'XLS_tasks': 'D:\рабочий стол\Основные папки\Разработка\Задачи.xlsx',
        'Dir_dev': 'D:\рабочий стол\Основные папки\Разработка',
        'Cntlm': 'D:\cntlm-0.92.3\_start.cmd',
        'Chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        'iexplore': 'C:\Program Files\Internet Explorer\iexplore.exe',
        'Train': 'D:\Projects\Train',
        'SapLogon': '"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"',
        'Lutz': 'D:\Projects\programmirovanie_na_python_4-e_izdanie_i_tom_fail_pdf_889705.pdf'
    }
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        self.vars = []
        self.paths = {}
        for key in startWork.demos:
            var = IntVar()
            Checkbutton(self, text=key, variable=var).pack(side=LEFT)
            self.paths[var._name] = startWork.demos[key]
            self.vars.append(var)

    # def fixWindowsPath(self, path):
    #     splitline = path.lstrip().split(' ')
    #     fixedpath = os.path.normpath(splitline[0])
    #     return ''.join([fixedpath] + splitline[1:])

    def start_task(self):
        # path = self.fixWindowsPath(path)
        for var in self.vars:
            if var.get() == 1:
                path = self.paths[var._name]
                os.startfile(path)
    def reset(self):
        for var in self.vars:
            var.set(0)

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='Start', command=self.start_task).pack(fill=BOTH)
        Button(frm, text='Reset', command=self.reset).pack(fill=BOTH)
        Quitter(frm).pack(fill=X)

if __name__ == '__main__': startWork().mainloop()








