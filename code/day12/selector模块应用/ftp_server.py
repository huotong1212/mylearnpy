import selectors
import socket
import os
import json

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()
    print('accept',conn)
    conn.setblocking(False) # 设置IO不阻塞
    sel.register(conn,selectors.EVENT_READ,read)


def read(conn,mask):
    try:
        data = conn.recv(1024)
        dic = json.loads(data.decode('utf-8'))
        print(repr(dic))
        filename = dic['filename']
        filesize = int(dic['filesize'])
        if not os.path.exists(filename):
            f = open(filename,'ab')
            length = 0
            while length < filesize:
                msg = conn.recv(1024)
                f.write(msg)
                length += len(msg)

        # if not data:
        #     raise Exception()
        # print('echoing', repr(data), 'to', conn)
        # conn.send(data.upper())  # Hope it won't block
    except Exception as e:
        print(e)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost',8090))
sock.listen(5)
sock.setblocking(False)

sel.register(sock,selectors.EVENT_READ,accept)
print('server......')

while True:
    event = sel.select()
    for key,mask in event:
        func = key.data
        print('mask',mask)
        func(key.fileobj,mask)

