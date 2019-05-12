
## 服务端
import socket

# 创建一个socket 基于网络，基于数据流
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定IP 和 端口号
phone.bind(('127.0.0.1',8000))

# 开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
phone.listen(5)

# 拿到一个链接和该链接的地址  -- 等电话
# 其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
print('启动服务端，等待监听......')
conn,addr = phone.accept()

# 接受套接字的数据。数据以字符串形式返回
data = conn.recv(1024)
print('-------->data:',data)

# 向客户端发送消息
conn.send(data.upper())

conn.close()
phone.close()









