# coding:utf-8
from multiprocessing import Process
import time, os

def run():
    print('子', os.getpid())


if __name__ == '__main__':
    p = Process(target=run)
    p.start()

    print('主', os.getpid()) # 主进程没有调用wait回收已经死掉的子进程的残存信息，这些子进程称为僵尸进程
    time.sleep(1000)