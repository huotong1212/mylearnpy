import selectors
import socket


class Myselector():
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.sock = socket.socket()
        self.sock.bind(('localhost', 8090))
        self.sock.listen(100)
        self.sock.setblocking(False)
        self.n = 0

        self.sel.register(self.sock, selectors.EVENT_READ, self.accept)
        print("server.....")

    def accept(self,sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)  # 设置IO不阻塞
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self,conn, mask):
        try:
            self.n += 1
            data = conn.recv(1024)  # Should be ready
            if not data:
                raise Exception
            print('echoing',self.n, repr(data), 'to', conn)
            conn.send(data)  # Hope it won't block
        except Exception as e:
            print('closing', conn)
            self.sel.unregister(conn)
            conn.close()

    def start(self):
        while True:
            events = self.sel.select()#[sock,,conn2]
            for key, mask in events:
                callback = key.data
                print(mask)
                callback(key.fileobj, mask)

if __name__ == '__main__':
    ms = Myselector()
    ms.start()