import threading,time
class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        event.isSet() or event.set()   # set设置flag为True,使wait通行
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set() # 这行代码确保event变成True
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(0.25)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")
if __name__=="__main__":
    event=threading.Event()
    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# 条件同步和条件变量同步差不多意思，只是少了锁功能，因为条件同步设计于不访问共享资源的条件环境。
# event=threading.Event()：条件环境对象，初始值 为False；
#
# 复制代码
# event.isSet()：返回event的状态值；
#
# event.wait()：如果 event.isSet()==False将阻塞线程；
#
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
#
# event.clear()：恢复event的状态值为False。