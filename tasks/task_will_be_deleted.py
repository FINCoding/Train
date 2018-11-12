class Thing(object):
    def __init__(self, name):
        self.name = name
        self.is_not_a = self.is_a = something()
        self.is_a_woman = self.is_a.woman
        self.is_a_man = self.is_a.man


class something:
    def __init__(self):
        self.woman = True
        self.man = False


if __name__ == '__main__':
    jane = Thing('Jane')
    print(jane.is_a.wooman)