# echo-client.py

import socket
from random import randint
from time import sleep

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def send_data(data: str):
    data = bytes(data, 'utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)
        assert s.recv(1024) == data, "transmission failed"


if __name__ == "__main__":
    for i in range(100):
         send_data(str(randint(1, 1000)))
         sleep(1)
