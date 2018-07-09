from socket import *
myHost = ''
myPort = 50008
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost,myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print('server connect by', address)

    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo=>' + data)
    connection.close()
