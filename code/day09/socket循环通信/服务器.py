
from socket import *

ip_sort = ('127.0.0.1',8090)
back_log = 5
buffer_size = 1024


# 创建一个socket
tcp_server = socket(AF_INET,SOCK_STREAM)
# 绑定ip 和 端口号
tcp_server.bind(ip_sort)
# 设置back_log 半连接挂起数量
tcp_server.listen(back_log)
print('服务器启动了......')
# 设置监听，服务器阻塞
while True:
    conn,addr = tcp_server.accept()
    print('双向链接是',conn)
    print('客户端地址',addr)

    while True:
        # 接受数据
        try:
            data = conn.recv(1024)
            print('data from client',data.decode('utf-8'))

            #发送数据
            conn.send(data.upper())
        except Exception:
            break  # 防止客户端突然断开链接导致 conn为空，继而产生异常

conn.close()
tcp_server.close()