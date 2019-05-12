
import socketserver
from socketserver import BaseRequestHandler

class MyServer(BaseRequestHandler):
    def handle(self):
        conn = self.request
        addr = self.client_address

        print('server',self.server)
        print('conn:',conn)
        print('addr',addr)

        while True:
            try:
                # 接收消息
                data = conn.recv(1024)
                if not data: break

                print('data from client:',data)

                # 发送消息给客户端
                conn.sendall(data.upper())
            except Exception as e:
                print(e)
                break

ip_port = ('127.0.0.1',8000)

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(ip_port,MyServer)  # 多线程
    print('服务器启动了.....')
    # s = socketserver.ForkingTCPServer(ip_port,MyServer) # 多进程
# BaseServer.serve_forever(poll_interval=0.5): 处理请求，直到一个明确的shutdown()请求。
# 每poll_interval秒轮询一次shutdown。忽略self.timeout。如果你需要做周期性的任务，建议放置在其他线程。
    s.serve_forever()

