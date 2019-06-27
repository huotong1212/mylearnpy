# 主进程创建守护进程
#
# 　　其一：守护进程会在主进程代码执行结束后就终止
#
# 　　其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError:
# daemonic processes are not allowed to have children
#
# 注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止

from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name,num):
        super().__init__()
        self.name=name
        self.num = num
    def run(self):
        print('%s is piaoing' %self.name)
        i = 0
        while i < self.num:
            time.sleep(1)
            i += 1
            print('i:', i)
        time.sleep(random.randrange(1,3))
        print('%s is piao end' %self.name)
        print('i:',i)

if __name__=='__main__':
    p=Piao('egon',3)
    p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    time.sleep(8) # 主进程结束后，守护进程立即终止，不管有没有执行完毕
    print('p守护进程还活着吗？',p.is_alive()) # 测试守护进程代码运行完之后，主进程还没运行完，看守护进程还活着吗
    print('主')

### 如果主进程还没运行完毕，守护进程就运行完毕了，那守护进程就算挂掉了