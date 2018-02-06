#!/usr/local/bin/python
from sys import argv
from scanfile import sacnner

class UnknownCommand(Exception): pass
def processLine(line):
    if line[0] == '*':
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])
    else:
        raise UnknownCommand(line)

filename = 'D:\Train\hillbillies.txt'
if len(argv) == 2: filename = argv[1]
sacnner(filename, processLine)

