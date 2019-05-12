from multiprocessing import Process,Pipe

import time,os
def adder(p,name):
    server,client=p
    client.close()
    while True:
        try:
            x,y=server.recv()
        except EOFError:
            server.close()
            break
        res=x+y
        server.send(res)
    print('server done')
if __name__ == '__main__':
    server,client=Pipe()

    c1=Process(target=adder,args=((server,client),'c1'))
    c1.start()

    server.close()

    client.send((10,20))
    print(client.recv())
    client.close()

    c1.join()
    print('主进程')
#注意：send()和recv()方法使用pickle模块对对象进行序列化。

# 管道可以用于双向通信，利用通常在客户端/服务器中使用的请求／响应模型或远程过程调用，
# 就可以使用管道编写与进程交互的程序