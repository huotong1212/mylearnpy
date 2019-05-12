#这种程序虽说解决了单线程并发，但是大大的占用了cpu
from socket import *
import time
severt = socket(AF_INET,SOCK_STREAM)
severt.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
severt.bind(('127.0.0.1',8080))
severt.listen(5)
severt.setblocking(False) #默认是True  (如果是False,套接字里的一些阻塞操作都变成非阻塞的)
print('startting....')
conn_l = []
del_l =[]
while True:
    try:
        print(conn_l)
        conn,addr = severt.accept() #收不到数据的时候才出异常
        print(conn)
        conn_l.append(conn)
    except BlockingIOError:  #吧收不到数据的那段时间利用起来（利用他收不到
        #数据的时候，才干下面的for循环）
       for conn in conn_l:
            try:
                data = conn.recv(1024)
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:  #端开链接的错误（如果突然断开链接，会报错
                                           #就先添加到列表里面去，完了吧链接给清除了）
                 del_l.append(conn)
       for obj in del_l:
             obj.close()
             conn_l.remove(obj)
       del_l.clear()