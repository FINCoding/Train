import sys, glob
import os
path = 'D:\\Projects\\Train\\Test\\'
marker = ':' * 20 + 'textpak=>'

def pack(ofile, ifiles):
    output = open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        input = open(name, 'r').read()
        if input[-1] != '\n': input += '\n'
        output.write(marker + name + '\n')
        output.write(input)

if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        ifiles += glob.glob(patt)
    # for patt in ['spam.txt', 'eggs.txt', 'ham.txt']:
    #     ifiles += glob.glob(path+patt)
    pack(sys.argv[1], ifiles)
    # pack('packed.txt', ifiles)

