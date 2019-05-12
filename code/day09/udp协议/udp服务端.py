
from socket import *

ip_sort = ('127.0.0.1',8090)
buffer_size = 1024

udp_server = socket(AF_INET,SOCK_DGRAM)  # 数据报式的套接字
udp_server.bind(ip_sort)
print('udp服务端启动了.......')
while True:
    data,addr = udp_server.recvfrom(buffer_size)
    print('data from client:',data,addr)

    udp_server.sendto(data.upper(),addr)

udp_server.close()