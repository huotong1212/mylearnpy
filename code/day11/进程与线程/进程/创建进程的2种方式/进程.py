
from multiprocessing import Process

import os
# os.getpid() 获取进程ID

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

## 创建进程的方法一
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
    # 用start()方法启动，这样创建进程比fork()还要简单。
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')
