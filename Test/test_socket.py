# import socket
from socket import AF_INET, SOCK_STREAM, create_connection
port = 50009
host = 'localhost'
timeout = None
address = (host, port)
conn = create_connection((host,port),timeout)#,('172.30.6.163', 80))
print('Hello')

#### рабочий код ###
# from socket import socket, AF_INET, SOCK_STREAM, create_connection
#
# port = 50009
# host = 'localhost'
# timeout = None
#
# def server():
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(('', port))
#     sock.listen(5)
#     while True:
#         conn, addr = sock.accept()
#         data = conn.recv(1024)
#         reply = 'server got: [%s]' % data
#         conn.send(reply.encode())
#
# def client(name):
#     sock = create_connection((host,port),timeout)
#     sock.send(name.encode())
#     reply = sock.recv(1024)
#     sock.close()
#     print('client got: [%s}' % reply)
#
# if __name__ == '__main__':
#     from threading import  Thread
#     sthread = Thread(target=server)
#     sthread.daemon = True
#     sthread.start()
#     for i in range(5):
#         Thread(target=client, args=('client%s' % i,)).start()