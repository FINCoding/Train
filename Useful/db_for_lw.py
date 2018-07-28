import sqlite3
from tkinter import *
from quitter import Quitter
tab_col = ['words', 'descrip']
conn = sqlite3.connect('learning_words.db')
c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS twords
#              (id INTEGER NOT NULL PRIMARY KEY, words text, description text, box integer, date text)''')
#
# c.execute("INSERT INTO twords VALUES (1,'Hello','привет','1', '2018-07-11')")

# conn.commit()

# conn.close()
class View(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.vars = self.makeWidgets()
        print(vars)
        self.makeToolBar()

    def makeWidgets(self):
        widgets = Frame(self)
        widgets.pack(side=TOP, expand=YES, fill=BOTH)
        left = Frame(widgets)
        left.pack(side=LEFT, expand=YES, fill=X)
        right = Frame(widgets)
        right.pack(side=RIGHT, expand=YES, fill=X)
        variables = []
        for col in tab_col:
            Label(left, text=col, width=5).pack(expand=YES, fill=X, side=TOP)
            ent = Entry(right)
            ent.pack(side=TOP, fill=X)
            var = StringVar()
            ent.config(textvariable=var)
            var.set('')
            variables.append(var)
        return variables

    def makeToolBar(self):
        toolbar = Frame(self, relief=SUNKEN, bg='beige', bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Save', command=self.save_word).pack(side=LEFT)
        Quitter(toolbar).pack(side=RIGHT)

    def get_id(self):
        c.execute('SELECT max(id) FROM twords')
        return c.fetchone()[0]

    def save_word(self):
        where = ''
        # n = 1
        id = self.get_id() + 1
        date = "00000000"
        where = "%d, '%s', '%s', %d, '%s'" % (int(id), self.vars[0].get(), self.vars[1].get(), 1, date)
        """for key in self.vars.keys():
            if n == len(self.vars):
                where += "%s = '%s'" % (key, self.vars[key].get())
            else:
                where += "%s = '%s' AND " % (key, self.vars[key].get())
            n += 1"""
        print(where)
        self._ins_db(where)

    def _ins_db(self, where):
        c.execute("INSERT INTO twords VALUES (%s)" % (where))#VALUES (1,'Hello','привет','1', '2018-07-11')")
        conn.commit()
        conn.close()


if __name__ == '__main__':
    View().mainloop()