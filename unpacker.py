import sys
import os
from packer import marker
mlen = len(marker)

def unpack(ifile, prefix='-new'):
    for line in open(ifile):
        if line[:mlen] != marker:
            output.write(line)
        else:
            nf = os.path.basename(line[mlen:-1])
            nfw = os.path.splitext(nf)
            nd = os.path.dirname(line[mlen:-1])
            name = nd + '\\' + nfw[0] + prefix + nfw[1]
            # name = prefix + line[mlen:-1]
            print('creating:',name)
            output = open(name, 'w')

if __name__ == '__main__':
    unpack(sys.argv[1])
    # unpack('D:\\Projects\\Train\\packed.txt')