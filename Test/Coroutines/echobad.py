from socket import socket, AF_INET, SOCK_STREAM

from pyos5 import NewTask, ReadWait, WriteWait

def handle_client(client, addr):
    print("Connection from" , addr)
    while True:
        data = client.recv(65536)
        if not data:
            break
        client.send(data)
    client.close()
    print("client closed")
    yield

def server(port):
    print("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
            client, addr = sock.accept()
            yield NewTask(handle_client(client, addr))

