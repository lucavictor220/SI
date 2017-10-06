from socket import *

HOST_NAME = 'localhost'
PORT = 8080


class TcpServer:
    def __init__(self):
        self.server_sock = socket(AF_INET, SOCK_STREAM)
        self.server_sock.bind((HOST_NAME, PORT))
        self.server_sock.listen(10)

    def accept_connections(self):
        print("Waiting for connection on port %s" % PORT)
        for i in range(1, 20):
            (client_socket, addr) = self.server_sock.accept()
            print("Connection received...")
            client_socket.sendall('Connected!\n'.encode('utf-8'))

        self.server_sock.close()