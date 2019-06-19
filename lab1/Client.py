from constants.Config import config

from clients.TcpClient import TcpClient
from clients.UdpClient import UdpClient


class Client:
    def __init__(self):
        pass

    @classmethod
    def factory(cls, protocol):
        if protocol == '-t':
            return TcpClient(config['HOST_NAME'], config['PORT'])
        if protocol == '-u':
            return UdpClient(config['HOST_NAME'], config['PORT'])

        return TcpClient(config['HOST_NAME'], config['PORT'])
