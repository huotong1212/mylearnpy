import socket
import select
sk=socket.socket()
sk.bind(("127.0.0.1",9904))
sk.listen(5)

while True:
    r,w,e=select.select([sk,sk],[],[],5)
    r=[sk,]
    for i in r:
        conn,add=i.accept()
        print(conn)
        print("hello")

    print('>>>>>>')