import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 8080))

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    if message:
        print message