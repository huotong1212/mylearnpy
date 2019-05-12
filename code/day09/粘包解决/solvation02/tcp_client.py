#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import socket,time
import struct
from functools import partial

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break

    # 客户端先发送命令
    s.send(msg.encode('utf-8'))

    # 客户端接受4给长度的字节
    length=s.recv(4)

    # 使用struct解析长度
    num = struct.unpack('i',length)[0]

    # 客户端循环接受服务端发送的数据
    result = ''.join(iter(partial(s.recv,1024),b''))
    print('执行结果：',result.decode('gbk'))


