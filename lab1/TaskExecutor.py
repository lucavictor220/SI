from time import sleep
from socket import error
from constants.Config import Config
from clients.TcpClient import TcpClient
from servers.TcpServer import TcpServer
from constants.Config import Config as ConfigurationClass
import os


class TaskExecutor:
    def __init__(self, client):
        self.client = client


    def send_message(self):
        self.client.get_connection()
        self.client.send_message(config.config['MESSAGE'])

    @staticmethod
    def ping():
        config_class = ConfigurationClass()
        print('Start ping command!\n')
        for _ in range(0, Config.config['MAX_NR_OF_MESSAGES']):
            client = TcpClient(config_class.config['HOST_NAME'], config_class.config['PORT'])
            client.get_connection()
            client.send_message(config_class.config['MESSAGE'])
            client.client_socket.close()
            print("Wait a second before sending new message")
            sleep(config_class.config['TIME_INTERVAL'])


    @staticmethod
    def scan():
        open_ports = []
        print('Start scan of ports')
        for index in range(*config_class.config['PORTS_TO_SCAN']):
            try:
                print("Trying to connect to port: %s" % index)
                client = TcpClient(config_class.config['HOST_NAME'], config_class.config['PORT'])
                client.client_socket.connect((config['HOST_NAME'], index))
                open_ports.append(index)
                client.client_socket.close()
            except error, exc:
                print('Error', exc)

        print("\n\n For the hostname %s the following ports are open:\n" % config['HOST_NAME'])
        print(open_ports)

    @staticmethod
    def server():
        server = TcpServer(config['HOST_NAME'], config['PORT'])
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

    @staticmethod
    def proxy():
        nr_of_connections = 1
        nr_of_messages = 0
        proxy = TcpServer(config['HOST_NAME'], config['PORT'])
        print("Proxy is up and waiting...")
        while True:
            print("Waiting for %i connection..." % nr_of_connections)
            (client_socket, addr) = proxy.server_sock.accept()
            source_message = client_socket.recv(1024)
            print("message: %s" % source_message)
            server_connection = TcpClient(config['TARGET_HOST_NAME'], config['TARGET_PORT'])
            server_connection.get_connection()
            server_connection.send_message(source_message)
            print("Close connection nr %i" % nr_of_connections)
            nr_of_messages += 1
            nr_of_connections += 1
            client_socket.close()

