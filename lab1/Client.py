from constants.config import config

from clients.TcpClient import TcpClient
from clients.UdpClient import UdpClient


class Client:
    @classmethod
    def factory(cls, protocol):
        client = None
        if protocol == '-t':
            client = TcpClient(config['HOST_NAME'], config['PORT'])
        if protocol == '-u':
            client = UdpClient(config['HOST_NAME'], config['PORT'])

        return client
