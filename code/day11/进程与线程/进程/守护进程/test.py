from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name):
        self.name=name
        super().__init__()
    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,3))

        print('%s is piao end' %self.name)


if __name__=='__main__':
    p=Piao('egon')
    p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    time.sleep(1)
    print('主')
