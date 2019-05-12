import threading,time
class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()
if __name__=="__main__":
    semaphore=threading.Semaphore(5)
    thrs=[]
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()

# 信号量用来控制线程并发数的，BoundedSemaphore或Semaphore管理一个内置的计数 器，
# 每当调用acquire()时-1，调用release()时+1。
#
# 计数器不能小于0，当计数器为 0时，acquire()将阻塞线程至同步锁定状态，
# 直到其他线程调用release()。(类似于停车位的概念)
#
# BoundedSemaphore与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值
# 是否超过了计数器的初始值，如果超过了将抛出一个异常