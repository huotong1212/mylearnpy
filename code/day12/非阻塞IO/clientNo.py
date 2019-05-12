from socket import *
client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))