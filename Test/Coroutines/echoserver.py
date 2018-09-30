# import socket
from socket import socket, AF_INET, SOCK_STREAM

from pyos5 import NewTask, ReadWait, WriteWait

def Accept(sock):
    yield ReadWait(sock)
    yield sock.accept()

def Send(sock, buffer):
    while buffer:
        yield WriteWait(sock)
        len = sock.send(buffer)
        buffer = buffer[len:]

def Recv(sock, maxbytes):
    yield ReadWait(sock)
    yield sock.recv()

def handle_client(client, addr):
    print("Connection from" , addr)
    while True:
        data = yield Recv(client, 65536)
        if not data:
            break
        yield Send(client, data)
    print("client closed")
    client.close()

def server(port):
    print("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        client, addr = yield Accept(sock)
        yield NewTask(handle_client(client, addr))

