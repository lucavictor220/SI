from socket import *


class TcpClient:
    def __init__(self, host_name, port):
        self.hostname = host_name
        self.port = port
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def get_connection(self):
        try:
            self.client_socket.connect((self.hostname, self.port))
        except Exception:
            print 'Connection to the host: %(host)s, port: %(port)d failed.' % {"host": self.hostname, "port": self.port}

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))

