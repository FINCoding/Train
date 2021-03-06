import os, sys

class FileVisitor:
    def __init__(self, context=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.trace = trace

    def run(self, startDir=os.curdir, reset=True):
        if reset: self.reset()
        for (thisDir, dirHere, filesHere) in os.walk(startDir):
            self.visitdir(thisDir)
            for frame in filesHere:
                fpath = os.path.join(thisDir, frame)
                self.visitfile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        self.dcount += 1
        if self.trace > 0: print(dirpath, '...')

    def visitfile(self, filepath):
        self.fcount += 1
        if self.trace > 1: print(self.fcount, '=>', filepath)

class SearchVisitor(FileVisitor):
    skipexts = []
    testexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']
    # skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe']

    def __init__(self, searchkey, trace=2):
        FileVisitor.__init__(self, searchkey, trace)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.testexts:
            return ext in self.testexts
        else:
            return ext not in self.skipexts

    def visitfile(self, fname):
        FileVisitor.visitfile(self, fname)
        if not self.candidate(fname):
            if self.trace > 0: print('Skipping', fname)
        else:
            text = open(fname).read()
            if self.context in text:
                self.visitmatch(fname, text)
                self.scount += 1

    def visitmatch(self, fname, text):
        print('%s has %s' % (fname, self.context))

if __name__ == '__main__':
    dolist = 1
    dosearch = 2
    donext  = 4

    def selftest(testmask):
        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            # visitor.run(sys.argv[2])
            visitor.run('D:\Projects\Train\Test')
            print('Visited %d files and %d dirs' % (visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace=0)
            visitor.run(sys.argv[2])
            print('Found in %d files, visited %d' % (visitor.scount, visitor.fcount))

    # selftest(int(sys.argv[1]))
    selftest(int(2))