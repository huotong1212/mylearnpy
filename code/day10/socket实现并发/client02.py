
import socket

ip_port = ('127.0.0.1',8000)

c2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c2.connect(ip_port)

while True:
    msg = input('>>:').strip()
    if not msg: continue
    if msg == 'exit': break

    c2.send(msg.encode('utf-8'))

    data = c2.recv(1024)
    print('data from server:',data.decode('utf-8'))

c2.close()