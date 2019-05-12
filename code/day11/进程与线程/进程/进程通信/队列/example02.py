'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

from multiprocessing import Process,Queue
import time
q=Queue(3)


#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full()) #满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了