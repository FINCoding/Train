import os
import fnmatch

wwwlog = open("log.txt")
# bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
# bytes = (int(x) for x in bytecolumn if x != '-')
# print(sum(bytes))
#########
# def gen_find(filepat, top):
#     for path, dirkist, filelist in os.walk(top):
#         for name in fnmatch.filter(filelist, filepat):
#             yield os.path.join(path, name)
#
# pyfiles = gen_find("*.py", "D:\\Projects\\")
# [print(pyfile) for pyfile in pyfiles]
#######

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

loglines = follow(wwwlog)
[print(line) for line in loglines]



