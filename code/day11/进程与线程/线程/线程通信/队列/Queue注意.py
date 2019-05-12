import threading,time

# 列表是线程不安全的
li=[1,2,3,4,5]

def pri():
    while li:
        a=li[-1]
        print(a)
        time.sleep(1)
        try:
            li.remove(a)
        except:
            print('----',a)

t1=threading.Thread(target=pri,args=())
t1.start()
t2=threading.Thread(target=pri,args=())
t2.start()