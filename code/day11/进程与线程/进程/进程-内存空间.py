
# 进程之间的内存空间是隔离的

from multiprocessing import Process

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
    p1 = Process(target=work,args=(10,'Alex',))
    p2 = Process(target=work,args=(8,'Danel',))

    p1.start()
    p2.start()

    p1.join()

    print('主进程结束了......')