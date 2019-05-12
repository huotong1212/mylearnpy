import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print ("Begin listening to %s. %s" %(func,ctime()))
        sleep(4)
        print("end listening %s"%ctime())

def move(func):
    for i in range(2):
        print ("Begin watching at the %s! %s" %(func,ctime()))
        sleep(5)
        print('end watching %s'%ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        # t.setDaemon(True)
        t.start()
        # t.join()
    # t1.join()
    t2.join()########考虑这三种join位置下的结果？
    print ("all over %s" %ctime())