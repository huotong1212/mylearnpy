from multiprocessing import Process,Pipe

import time,os
def consumer(p,name):
    left,right=p
    left.close()
    while True:
        try:
            baozi=right.recv()
            print('%s 收到包子:%s' %(name,baozi))
        except EOFError:
            right.close()
            break
def producer(seq,p):
    left,right=p
    right.close()
    for i in seq:
        left.send(i)
        # time.sleep(1)
    else:
        left.close()
if __name__ == '__main__':
    left,right=Pipe()

    c1=Process(target=consumer,args=((left,right),'c1'))
    c1.start()


    seq=(i for i in range(10))
    producer(seq,(left,right))

    right.close()
    left.close()

    c1.join()
    print('主进程')

# 基于管道实现进程间通信（与队列的方式是类似的，队列就是管道加锁实现的）
'''
注意：生产者和消费者都没有使用管道的某个端点，就应该将其关闭，
如在生产者中关闭管道的右端，在消费者中关闭管道的左端。如果忘记执行这些步骤，
程序可能再消费者中的recv()操作上挂起。管道是由操作系统进行引用计数的,
必须在所有进程中关闭管道后才能生产EOFError异常。
因此在生产者中关闭管道不会有任何效果，付费消费者中也关闭了相同的管道端点。
'''