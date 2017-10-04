from TcpClient import TcpClient
from UdpClient import UdpClient
from config import config


class Client:
    @classmethod
    def factory(cls, protocol):
        client = None
        if protocol == '-t':
            client = TcpClient(config)
        if protocol == '-u':
            client = UdpClient(config)

        return client
