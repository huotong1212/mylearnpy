from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()

    p1.join()
    q.put(None) #发送结束信号
    print('主')

# 注意：结束信号None，不一定要由生产者发，主进程里同样可以发，但主进程需要等生产者结束后才应该发送该信号
# 主进程在生产者生产完毕后发送结束信号None