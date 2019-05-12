#介绍
# The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously. ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock but also means that only picklable objects can be executed and returned.
#
# class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None)
# An Executor subclass that executes calls asynchronously using a pool of at most max_workers processes. If max_workers is None or not given, it will default to the number of processors on the machine. If max_workers is lower or equal to 0, then a ValueError will be raised.


#用法
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import os,time,random
def task(n):
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':

    executor=ProcessPoolExecutor(max_workers=3)

    futures=[]
    for i in range(11):
        '''
        submit(fn, *args, **kwargs)
        异步提交任务
        '''
        future=executor.submit(task,i)
        futures.append(future)
    '''
        shutdown(wait=True) 
        相当于进程池的pool.close()+pool.join()操作
        wait = True，等待池内所有任务执行完毕回收完资源后才继续
        wait = False，立即返回，并不会等待池内的任务执行完毕
        但不管wait参数为何值，整个程序都会等到所有任务执行完毕
    '''
    executor.shutdown(True)

    print('+++>')
    for future in futures:
        print(future.result())

