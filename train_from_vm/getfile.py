import sys, os, time, _thread as thread
from socket import *

blksz = 1024
defaultHost = 'localhost'
defaultPort = 50001

helptext = """
Usage...
server=> getfile.py -mode server [-port nnn][-host -hhh|localhost]
client=> getfile.py [-mode client] -file fff [-port nnn][-host -hhh|localhost]"""

def now():
    return time.asctime()

def parsecommandline():
    dict = {}
    # a = ['getfile.py', '-mode', 'client', '-file', 'D:\Projects\Train\Internet\webserver.py', '-port', '50001', '-host', '172.30.6.163']
    print(sys.argv)
    args = sys.argv[1:]
    # args = a[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def parsecommandline1():
    dict = {}
    args = sys.argv[1:]
    # print(sys.argv)
    # print(args)
    while len(args) >= 2:
        dict[args[0]] = args[1]
        print(dict)
        args = args[2:]
        # print(args)
    # print (args)

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())
    dropdir = os.path.split(filename)[1]
    # dropdir = os.path.basename(filename)
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print('Clinet got', filename, 'at', now())

def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]

    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print('Error downloading file on server:', filename)
    clientsock.close()

def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print('Server connected by', clientaddr, 'at', now())
        thread.start_new_thread(serverthread, (clientsock,))

def main(args):
    host = args.get('-host', defaultHost)
    port = int(args.get('-port', defaultPort))
    if args.get('-mode') == 'server':
        if host == 'localhost': host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)

if __name__ == '__main__':
    args = parsecommandline()
    # args = parsecommandline1()
    main(args)

