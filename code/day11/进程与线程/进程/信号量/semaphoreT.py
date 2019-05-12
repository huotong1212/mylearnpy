# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去，
# 如果指定信号量为3，那么来一个人获得一把锁，计数加1，当计数等于3时，后面的人均需要等待。
# 一旦释放，就有人可以获得一把锁
#  信号量与进程池的概念很像，但是要区分开，信号量涉及到加锁的概念

from multiprocessing import Process,Semaphore
import time,random

def go_wc(sem,user):
    sem.acquire()
    print('%s 占到一个茅坑' %user)
    time.sleep(random.randint(0,3)) #模拟每个人拉屎速度不一样，0代表有的人蹲下就起来了
    sem.release()

if __name__ == '__main__':
    sem=Semaphore(5)
    p_l=[]
    for i in range(13):
        p=Process(target=go_wc,args=(sem,'user%s' %i,))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()
    print('============》')

# 信号量Semahpore（同线程一样）