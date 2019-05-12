
# 线程之间的内存空间是共同的

import threading

n = 100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了

def work(s,name):
    global n
    print('%s has started......'%name)
    i = 0
    while i < s:
        n += 1
        i += 1
    print('%s num n value:%d'%(name,n))

if __name__ == "__main__":
    p1 = threading.Thread(target=work,args=(10,'Alex',))
    p2 = threading.Thread(target=work,args=(8,'Danel',))

    p1.start()
    p2.start()

    p1.join()

    print('主线程结束了......')