from socket import *


class UdpClient:
    def __init__(self, host_name, port):
        self.hostname = host_name
        self.port = port
        self.client_socket = self.create_client()

    def create_client(self):
        client_socket = socket(AF_INET, SOCK_DGRAM)
        client_socket.settimeout(2)
        return client_socket

    def send_message(self, message):
        self.client_socket.sendto(message.encode('utf-8'), (self.hostname, self.port))