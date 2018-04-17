import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable

def fixWindowsPath(cmdline):
    splitline = cmdline.lstrip().split(' ')
    fixedpath = os.path.normpath(splitline[0])
    return ''.join([fixedpath] + splitline[1:])

def getProgramName(pypath):
    splitline = pypath.lstrip().split('\\')
    progname = os.path.normpath(splitline[-1])
    return progname

class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self):
        self.announce(self.what)
        self.run(self.where)
    def announce(self, text):
        print(text)
    def run(self, cmdline):
        assert False, 'run must be defined'

class System(LaunchMode):
    def run(self,cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pypath, cmdline))

class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)

class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pypath, [pyfile]+cmdline)

class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)

class StartArgs(LaunchMode):
    def run(selfself, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)

class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class Top_level(LaunchMode):
    def run(self, cmdline):
        assert False, 'escho ne realizovano'


if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass

def selftest():
    global pypath
    file = 'D:\Projects\Train\\test.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()
    pypath = getProgramName(pypath)
    input('system mode...')
    System(file, file)()

    if sys.platform[:3] == 'win':
        input('dos start mode...')
        StartArgs(file, file)()

if __name__ == '__main__': selftest()
