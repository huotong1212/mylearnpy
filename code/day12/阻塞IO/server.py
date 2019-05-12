from socket import *
server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
print('start runnig...')
while True:
    conn,addr = server.accept()  #IO操作 在这accept的时候不能干recv的活
    print(addr)
    while True:
        try:
            data = conn.recv(1024)  #IO操作
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
server.close()

# 我们以前写的这个就是阻塞的IO模型：一旦阻塞了就在那卡着
# 直到等到数据已经到了操作系统，操作系统再从内核拷贝给应用程序
# 阻塞IO在那两个阶段全都阻塞住了

# 服务端