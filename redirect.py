import sys

class Output:
    def __init__(self):
        self.text = ''
    def write(self, string):
        self.text += string
    def writelines(self, lines):
        for line in lines: self.write(line)

class Input:
    def __init__(self, input=''):
        self.text = input
    def read(self, size=None):
        if size == None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')
        res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        # if eoln == 1:
        #     res, self.text = self.text, ''
        # else:
        #     res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res

def redirect(function, pargs, kargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        # sys.stdin, sys.stdout = savestreams
        sys.stdin, sys.stdout
    return (result, output)

from teststreams import *
if __name__ == '__main__':
    (result, output) = redirect(interact, (), {}, '4\n5\n6\n')
    print(result)
    print(output)