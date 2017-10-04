import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_sock.bind(('127.0.0.1', 8080))
server_sock.listen(0)
print("Waiting for connection...")
(client_socket, addr) = server_sock.accept()
client_socket.sendall('Connected!\n'.encode('utf-8'))

while True:
    data = client_socket.recv(1024)
    if data:
        print(data.decode('utf-8'))

client_socket.close()
server_sock.close()