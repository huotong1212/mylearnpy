
from socket import *

ip_sort = ('127.0.0.1',8090)
back_log = 5
buffer_size = 1024

# 创建一个socket
tcp_client = socket(AF_INET,SOCK_STREAM)
# 连接服务器
tcp_client.connect(ip_sort)
while True:
    msg = input('请输入：').strip()

    if not msg: continue  # 不允许什么也不发送
    tcp_client.send(msg.encode('utf-8'))
    data = tcp_client.recv(1024)
    print('data from server-->',data.decode('utf-8'))

tcp_client.close()