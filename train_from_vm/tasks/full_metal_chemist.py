class Atom(object):

    def __init__(self, elt, id_):
        self.element = elt
        self.id = id_

    def __hash__(self):      return self.id

    def __eq__(self, other): return self.id == other.id


class Molecule(object):
    pass

class Error(Exception):
    pass

class MoleculeError(Error):
    def __init__(self, name=''):
        self.name = name

class One(object):
    def __init__(self, my_list=[]):
        self.my_list = my_list

class Second(object):
    def __init__(self, my_list=[]):
        self.my_list = list(my_list)

if __name__ == '__main__':
    # m = Molecule()
    # m = Molecule("banana")
    # print(m.name)
    one1 = One()
    one1.my_list.append('A')
    print(one1.my_list)
    one2 = One()
    print(one2.my_list)
    sec1 = Second()
    sec1.my_list.append('B')
    print(sec1.my_list)
    sec2 = Second()
    print(sec2.my_list)
