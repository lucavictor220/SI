import socket

HOST_NAME = 'localhost'
PORT = 8081

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_sock.bind((HOST_NAME, PORT))
server_sock.listen(10)
i = 1
print("Listening...",  HOST_NAME, PORT)

while True:
    print("Waiting for connection nr %i..." % i)
    (client_socket, addr) = server_sock.accept()
    client_socket.sendall('Connected!\n'.encode('utf-8'))
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))
    print('Close connection nr %i' % i)
    client_socket.close()
    i += 1
