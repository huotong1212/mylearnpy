
import socket
import os
import json

sock = socket.socket()
sock.connect(('localhost',8090))



filename = 'modern.mkv'

dic = {'filename':filename,'filesize':os.stat(filename).st_size}

sock.send(json.dumps(dic).encode('utf-8'))

choice = sock.recv(1024)
if 'N' == choice:
    raise Exception

if os.path.exists(filename):
    with open(filename,'rb') as f:
        lenght = 0
        while lenght < os.stat(filename).st_size:
            data = f.read(1024)
            sock.send(data)
            lenght += len(data)

# while True:
    # data = input(">>:").strip()
    # sock.send(data.encode('utf-8'))
    #
    # data = sock.recv(1024)
    # print('data from server:',data)