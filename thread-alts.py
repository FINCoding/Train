import _thread

def action(i):
    print(i**2)

class Power:
    def __init__(self,i):
        self.i = i

    def action(self):
        print(self.i**4)

_thread.start_new_thread(action,(2,))
_thread.start_new_thread((lambda: action(3)), ())
obj=Power(2)
_thread.start_new_thread(obj.action,())
print('use')