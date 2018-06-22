from tkinter.messagebox import *
from tkinter.messagebox import *

from Useful.launchmodes import PortableLauncher, System
from scrolledtext import ScrolledText


class GuiMixin:
    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error!', text)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        showerror('Not implemented', 'Option not available')

    def quit(self):
        ans = self.question('Verify quit', 'Are you sure want to quit?')
        if ans:
            Frame.quit(self)

    def help(self):
        self.infobox('RTFM', 'See figure 1...')

    def selectOpenFile(self, file="", dir="."):
        return askopenfilename(initialdir=dir, initialfile=file)

    def selectSaveFile(self, file='', dir='.'):
        return asksaveasfilename(initialfile=file, initialdir=dir)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)

    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)()

    def browser(self, filename):
        new = Toplevel()
        view = ScrolledText(new, file=filename)
        view.text.config(height=30, width=85)
        view.text.config(fount=('courier', 10, 'normal'))
        new.title('Text Viewer')
        new.iconname('browser')

    '''
    def browser(self, filename):
        new = Toplevel()
        text = ScrolledText(new, height=30, width=85)
        text.config(font=('courier', 10, 'normal'))
        text.pack(expand=YES, fill=BOTH)
        new.title('Text Viewer')
        new.iconname('browser')
        text.insert('0.0', open(filename, 'r').read())
    '''
if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)
        def other(self):
             self.spawn('D:\\Projects\\Train\\guimixin.py')

    TestMixin().mainloop()
