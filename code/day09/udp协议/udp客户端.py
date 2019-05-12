
from socket import *

ip_sort = ('127.0.0.1',8090)
buffer_size = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)  # 数据报式的套接字
print('udp客户端启动了.....')
while True:
    msg = input('请输入：').strip()
    if not msg: continue
    udp_client.sendto(msg.encode('utf-8'),ip_sort)
    data,addr = udp_client.recvfrom(buffer_size)
    print('data from server:',data.decode('utf-8'))
