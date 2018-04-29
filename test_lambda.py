def simple():
    spam = 'ni'
    def action():
        print(spam)
    return action
act = simple()

def normal():
    def action():
        return spam
    spam = 'ni'
    return action
g = normal()

def odd():
    func = []
    for c in 'abcdefg':
        func.append((lambda: c))
    return func

if __name__ == '__main__':
    for func in odd():
        print(func(), end = ' ')
    # act()
    # print(g())

    
    
    

