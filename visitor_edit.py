import os, sys
from visitor import SearchVisitor

class EditVisitor(SearchVisitor):
    editor = r'D:\notepad\notepad++.exe'

    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    # visitor = EditVisitor(sys.argv[1])
    visitor = EditVisitor('Hello world!')
    # visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    visitor.run('D:\Projects\Train\Test')
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))
