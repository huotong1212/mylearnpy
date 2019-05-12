
### 创建进程的第二种方式

from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name):
        # self.name=name
        # super().__init__() #Process的__init__方法会执行self.name=Piao-1,
        #                    #所以加到这里,会覆盖我们的self.name=name
        super().__init__()
        self.name = name

    def run(self):
        print('%s piao start'%self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end'%self.name)

if __name__ == "__main__":

    p1 = Piao('egon')
    p2 = Piao('alex')
    p3 = Piao('Jark')

    p1.start()  # start会自动调用run
    p2.start()
    p3.start()

    print('主线程')

