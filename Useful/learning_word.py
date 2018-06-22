from tkinter import *
import sys

class View(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.boxes = Boxes()
        self.word = self.get_word()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets(self.word)
        self.visible = False
        self.descr_l = self.makeDescrWidgets()

    def get_word(self):
        return self.boxes.get_word()
        # return Boxes().get_word()

    def makeMenuBar(self):
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)
        Button(menubar, text='Quit', command=sys.exit).pack(side=RIGHT)
        Button(menubar, text='Description', command=self.visDescrWidgets).pack(side=LEFT)

    def makeToolBar(self):
        toolbar = Frame(self, relief=SUNKEN, bg='beige', bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Yes', command=self.known_word).pack(side=RIGHT)
        Button(toolbar, text='No', command=self.unknown_word).pack(side=LEFT)

    def makeWidgets(self, word):
        name = Label(self, text=word, width=40, height=2, relief=SUNKEN, bg='white')
        name.pack(expand=YES, fill=BOTH)

    def makeDescrWidgets(self):
        descr_l = Text(self, width=40, height=10, relief=SUNKEN, bg='white')
        descr_l.insert('1.0', self.boxes.get_descr())
        # Descr_L.pack(expand=YES, fill=BOTH)
        return descr_l

    def visDescrWidgets(self):
        if self.visible:
            self.descr_l.pack_forget()
            self.visible = False
        else:
            self.descr_l.pack(expand=YES, fill=BOTH)
            self.visible = True

    def known_word(self):
        self.boxes.next_box()
        # Boxes().next_box()

    def unknown_word(self):
        print('unknown word')
        pass

class Boxes:
    def __init__(self):
        self.DB = DB()
    def get_word(self):
        return self.DB.wdict['Hello']['translate']

    def get_descr(self):
        return self.DB.wdict['Hello']['translate']

    def next_box(self):
        box_count = 3
        a = self.DB.wdict['Hello']['box']
        if self.DB.wdict['Hello']['box'] < box_count:
            self.DB.modify_db('Hello', 1)
            print(self.DB.wdict['Hello']['box'])

    def set_first_box(self):
        pass

class DB:
    wdict = {'Hello':{'translate': 'привет', 'box': 1, 'date': '01012017'},
              'World':{'translate': 'мир', 'box': 1, 'date': '01012017'},
              'Winner':{'translate': 'победитель', 'box': 1, 'date': '01012017'},
              'Work':{'translate': 'работа', 'box': 1, 'date': '01012017'}}

    def modify_db(self, word, i):
        a = DB.wdict[word]['box']
        DB.wdict[word]['box'] += i


if __name__ == '__main__':
    View().mainloop()
