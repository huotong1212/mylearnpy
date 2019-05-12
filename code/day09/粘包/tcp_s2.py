#_*_coding:utf-8_*_

#接收方不及时接收缓冲区的包，造成多个包接收（
# 客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）
__author__ = 'Linhaifeng'
from socket import *
ip_port=('127.0.0.1',8080)

tcp_socket_server=socket(AF_INET,SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)


conn,addr=tcp_socket_server.accept()


data1=conn.recv(2) #一次没有收完整
data2=conn.recv(10)#下次收的时候,会先取旧的数据,然后取新的

print('----->',data1.decode('utf-8'))
print('----->',data2.decode('utf-8'))

conn.close()

