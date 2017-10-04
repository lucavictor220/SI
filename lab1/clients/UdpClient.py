from socket import *


class UdpClient:
    def __init__(self, config):
        self.hostname = config['HOST_NAME']
        self.port = config['PORT']
        self.client_socket = self.create_client()

    def create_client(self):
        client_socket = socket(AF_INET, SOCK_DGRAM)
        client_socket.settimeout(2)
        return client_socket

    def send_message(self, message):
        self.client_socket.sendto(message.encode('utf-8'), (self.hostname, self.port))