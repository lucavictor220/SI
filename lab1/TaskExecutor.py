from time import sleep
from socket import error
from constants.config import config
from clients.TcpClient import TcpClient
from servers.TcpServer import TcpServer
import os


class TaskExecutor:
    def __init__(self, client):
        self.client = client

    def send_message(self):
        self.client.get_connection()
        self.client.send_message(config['MESSAGE'])

    def ping(self):
        self.client.get_connection()
        print('Start ping command!\n')
        for _ in range(0, config['MAX_NR_OF_MESSAGES']):
            sleep(config['TIME_INTERVAL'])
            self.client.send_message(config['MESSAGE'])

    @staticmethod
    def scan():
        open_ports = []
        print('Start scan of ports')
        for index in range(config['PORTS_TO_SCAN'][0], config['PORTS_TO_SCAN'][1]):
            if index == 445:
                continue
            try:
                print("Trying to connect to port: %s" % index)
                client = TcpClient(config)
                client.client_socket.connect((config['HOST_NAME'], index))
                open_ports.append(index)
                client.client_socket.close()
            except error, exc:
                print('Error', exc)

        print("\n\n For the hostname %s the following ports are open:\n" % config['HOST_NAME'])
        print(open_ports)

    @staticmethod
    def server():
        server = TcpServer()
        server.accept_connections()

    def get_page(self):
        request = "GET / HTTP/1.1\nHost: %s\r\n\r\n" % config['HOST_NAME']
        print('# Get request on the host: %s' % config['HOST_NAME'])
        self.client.get_connection()
        self.client.send_message(request)
        webpage = ""
        while True:
            data = self.client.client_socket.recv(1024)
            print data
            webpage += data
            if data[-5:] == "0\r\n\r\n":
                print "DONE"
                break

        if not os.path.exists('webpages'):
            os.makedirs('webpages')
        file = open('webpages/webpage.html', 'w')
        file.write(webpage)
        file.close()

