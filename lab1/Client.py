from constants.config import config

from clients.TcpClient import TcpClient
from clients.UdpClient import UdpClient


class Client:
    @classmethod
    def factory(cls, protocol):
        client = None
        if protocol == '-t':
            client = TcpClient(config)
        if protocol == '-u':
            client = UdpClient(config)

        return client
