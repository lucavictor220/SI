from socket import *
from constants.config import config


class TcpServer:
    def __init__(self, host_name, port):
        self.server_sock = socket(AF_INET, SOCK_STREAM)
        self.server_sock.bind((host_name, port))
        self.server_sock.listen(10)
        self.client_socket = None

    def accept_connections(self):
        print("Waiting for connection on port %s" % config['PORT'])
        for i in range(1, 20):
            (self.client_socket, addr) = self.server_sock.accept()
            print("Connection received...")
            self.client_socket.sendall('Connected!\n'.encode('utf-8'))

        self.server_sock.close()

