import sys, pprint, os
from visitor import FileVisitor

class LineByType(FileVisitor):
    scrExts = []

    def __init__(self, trace=1):
        FileVisitor.__init__(self, trace=trace)
        self.scrLines = self.scrFiles = 0
        self.extSums = {ext: dict(files=0, lines=0) for ext in self.scrExts}

    def visitsource(self, fpath, ext):
        if self.trace > 0: print(os.path.basename(fpath))
        lines = len(open(fpath, 'rb').readlines())
        self.scrFiles += 1
        self.scrLines += lines
        self.extSums[ext]['files'] += 1
        self.extSums[ext]['lines'] += lines

    def visitfile(self, filepath):
        FileVisitor.visitfile(self, filepath)
        for ext in self.scrExts:
            if filepath.endswith(ext):
                self.visitsource(filepath, ext)
                break

class PyLines(LineByType):
    scrExts = ['.py', '.pyw']

class SourceLines(LineByType):
    scrExts = ['.py', '.pyw', '.html', '.c', '.h', '.cgi', '.i']

if __name__ == '__main__':
    walker = SourceLines()
    walker.run(sys.argv[1])
    # walker.run('D:\Projects\Train')
    print('Visited %d files and %d dirs' % (walker.fcount, walker.dcount))
    print('-' * 80)
    print('Source files=>%d' % (walker.scrFiles, walker.scrLines))
    print('By Types:')
    pprint.pprint(walker.extSums)
    print('\nCheck sums:', end=' ')
    print(sum(x['lines'] for x in walker.extSums.values()), end=' ')
    print(sum(x['files'] for x in walker.extSums.values()))
    print('\nPython only walk:')
    walker = PyLines(trace=0)
    walker.run(sys.argv[1])
    # walker.run('D:\Projects\Train')
    pprint.pprint(walker.extSums)
