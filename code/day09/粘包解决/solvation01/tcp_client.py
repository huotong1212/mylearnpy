#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break

    # 客户端先发送命令
    s.send(msg.encode('utf-8'))

    # 客户端获取到需要接受的数据的长度
    length=int(s.recv(1024).decode('utf-8'))

    # 客户端发送我已准备的好接受
    s.send('recv_ready'.encode('utf-8'))

    # 客户端循环接受服务端发送的数据
    send_size=0
    recv_size=0
    data=b''
    while recv_size < length:
        # 每次接受1024个字节，data表示此次接受了多少个字节，有可能小于1024
        data+=s.recv(1024)
        recv_size+=len(data)

    print(data.decode('utf-8'))

