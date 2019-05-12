#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import socket,subprocess
ip_port=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(ip_port)
s.listen(5)

while True:
    conn,addr=s.accept()
    print('客户端',addr)
    while True:
        msg=conn.recv(1024)
        if not msg:break
        res=subprocess.Popen(msg.decode('utf-8'),shell=True,\
                            stdin=subprocess.PIPE,\
                         stderr=subprocess.PIPE,\
                         stdout=subprocess.PIPE)
        err=res.stderr.read()
        if err:
            ret=err
        else:
            ret=res.stdout.read()

        # 服务端先计算返回数据的长度
        data_length=len(ret)
        # 服务端发送客户端需要读取的长度
        conn.send(str(data_length).encode('utf-8'))

        # 接受来自客户端的招呼
        data=conn.recv(1024).decode('utf-8')

        # 确认客户端已经准被好接受
        if data == 'recv_ready':
            conn.sendall(ret)
    conn.close()

