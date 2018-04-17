import sys, os, glob
dirname = 'D:\Projects\Train' if len(sys.argv) == 1 else sys.argv[1]

allsize = []
apply = glob.glob(dirname + os.sep + '*.py')
for filename in apply:
    filesize = os.path.getsize(filename)
    allsize.append((filesize, filename))
allsize.sort()
print(allsize[:2])
print(allsize[-2:])
for f in allsize:
    print(f)
