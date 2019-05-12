

from socket import *
import subprocess

ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024

tcp_socket_client = socket(AF_INET, SOCK_STREAM)
tcp_socket_client.connect(ip_port)


while True:
    cmd = input('>>:').strip()
    if not cmd: continue
    if cmd == 'quit': break

    tcp_socket_client.send(cmd.encode('utf-8'))
    cmd_back = tcp_socket_client.recv(BUFSIZE)
    print(cmd_back.decode('gbk'),end='')










