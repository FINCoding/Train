from tkinter import *
import sqlite3
import sys
from datetime import datetime

# class Controler:
#     def __init__(self):
#         self.display = View().mainloop()#???

class View(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.upd = 'X'
        self.boxes = Boxes()
        self.row = self.get_row()
        self.word = self.row[1]
        self.makeMenuBar()
        self.makeToolBar()
        self.displayWord = self.makeWidgets(self.word)
        self.visible = False
        self.descrWord = self.makeDescrWidgets()

    def get_row(self, id=0):
        return self.boxes.get_row(id)

    def makeMenuBar(self):
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)
        Button(menubar, text='Quit', command=sys.exit).pack(side=RIGHT)
        Button(menubar, text='Description', command=self.visDescrWidgets).pack(side=LEFT)

    def makeToolBar(self):
        toolbar = Frame(self, relief=SUNKEN, bg='beige', bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        part1 = Frame(toolbar, relief=SUNKEN, bg='beige', bd=2).pack(side=BOTTOM, fill=X)
        part2 = Frame(toolbar, relief=SUNKEN, bg='beige', bd=2).pack(side=BOTTOM, fill=X)
        part3 = Frame(toolbar, relief=SUNKEN, bg='beige', bd=2).pack(side=BOTTOM, fill=X)
        part4 = Frame(toolbar, relief=SUNKEN, bg='beige', bd=2).pack(side=BOTTOM, fill=X)
        part5 = Frame(toolbar, relief=SUNKEN, bg='beige', bd=2).pack(side=BOTTOM, fill=X)
        Button(part5, text='Exactly', command=self.exactlyKnownWord).pack(side=RIGHT)
        Button(part3, text='Yes', command=self.knownWord).pack(side=RIGHT)
        Button(part1, text='No', command=self.unknown_word).pack(side=LEFT)

    def makeWidgets(self, word):
        displayWord = Label(self, text=word, width=40, height=2, relief=SUNKEN, bg='white')
        displayWord.pack(expand=YES, fill=BOTH)
        return displayWord

    def makeDescrWidgets(self):
        descrWord = Text(self, width=40, height=10, relief=SUNKEN, bg='white')
        descrWord.insert('1.0', self.get_descr())
        return descrWord

    def get_descr(self):
        return self.row[2]

    def visDescrWidgets(self):
        if self.visible:
            self.descrWord.pack_forget()
            self.visible = False
        else:
            self.descrWord.pack(expand=YES, fill=BOTH)
            self.visible = True

    def knownWord(self):
        self.boxes.next_box()
        self.updateDisplay()

    def exactlyKnownWord(self):
        self.boxes.next_box(self.upd)
        self.updateDisplay()

    def updateDisplay(self, upd=None):
        id = 0
        if upd: id =  self.row[0]
        self.row = self.get_row(id)
        self.word = self.row[1]
        self.displayWord.config(text=str(self.word))
        self.descrWord = self.makeDescrWidgets()

    def unknown_word(self):
        self.updateDisplay(self.upd)

class Boxes:
    box_count = 3
    def __init__(self):
        self.DB = DB()

    def get_row(self, id=0):
        self.row = self.DB.get_row(id)
        return self.row

    def next_box(self, upBox=None):
        if self.row[3] < Boxes.box_count:
            if upBox: self.row[3] += 1
            self.DB.modify_db(self.row[0], self.row[3])

    def set_first_box(self):
        pass

class DB:
    conn = sqlite3.connect('learning_words.db')
    def __init__(self):
        self.curs = DB.conn.cursor()

    def get_row(self, id):
        if id:
            self.curs.execute('SELECT * FROM twords WHERE id > %s and date = (SELECT min(date) FROM twords)' % id)
        else:
            self.curs.execute('SELECT * FROM twords WHERE date = (SELECT min(date) FROM twords)')
        return (self.curs.fetchone())

    def modify_db(self, id, box):
        date = datetime.now()
        print(date.strftime("%Y%m%d"))
        self.curs.execute('UPDATE twords SET box = %d, date = %d WHERE id = %d' % (box, int(date.strftime("%Y%m%d")), id))
        self._commit()
        # self.curs.execute('SELECT * FROM twords WHERE id = %d' % id)
        # print(self.curs.fetchone())

    def _commit(self):
        DB.conn.commit()

if __name__ == '__main__':
    # conn = sqlite3.connect('learning_words.db')
    # cur = conn.cursor()
    # cur.execute("select * from twords")
    # for row in cur:
    #     print(row)
    View().mainloop()

