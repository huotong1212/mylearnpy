# _*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from socket import *
import subprocess

ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024

tcp_socket_server = socket(AF_INET, SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

while True:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)

    while True:
        try:
            cmd = conn.recv(BUFSIZE)
            # 若客户端断开连接cmd为空
            if len(cmd) == 0: break

            res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            if res.stderr:
                cmd_back = res.stderr.read()
            else:
                cmd_back = res.stdout.read()

            if not cmd_back:
                cmd_back = '执行成功'.encode('gbk')

            conn.send(cmd_back)

        except Exception as e:
            print(e)
            break













