import socket


class TcpClient:
    def __init__(self, config):
        self.hostname = config['HOST_NAME']
        self.port = config['PORT']
        self.client_socket = self.create_client()

    def create_client(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.hostname, self.port))
        return self.client_socket

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))