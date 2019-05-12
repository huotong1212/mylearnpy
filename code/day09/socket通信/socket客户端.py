
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8000))  # 拨通电话，服务端的IP和地址

# 向服务端发生消息
phone.send('hello'.encode('utf-8'))

# 接受来自服务端的消息
data = phone.recv(1024)

print('data from server--->',data)
