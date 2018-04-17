import sys, os, pprint
trace = False
dirname = 'D:\\' if len(sys.argv) == 1 else sys.argv[1]

allsize = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            filesize = os.path.getsize(fullname)
            allsize.append((filesize, fullname))



allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])
for f in allsize:
    print(f)
