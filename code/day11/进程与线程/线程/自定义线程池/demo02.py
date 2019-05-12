#!/usr/bin/env python
# -*- coding:utf-8 -*-

import queue
import threading
import contextlib
import time

StopEvent = object()

class ThreadPool(object):

    def __init__(self, max_num, max_task_num = None):
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        self.max_num = max_num
        self.cancel = False
        self.terminal = False
        self.generate_list = []
        self.free_list = []

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if self.cancel:
            return
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        w = (func, args, callback,)#主线程
        self.q.put(w)#主线程

    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread()
        self.generate_list.append(current_thread)

        event = self.q.get()#if q为空，则阻塞住，一直等到有任务进来并把它取出来
        while event != StopEvent:

            func, arguments, callback = event
            try:
                result = func(*arguments)
                success = True
            except Exception as e:
                success = False
                result = None

            if callback is not None:
                try:
                    callback(success, result)
                except Exception as e:
                    pass

            with self.worker_state(self.free_list, current_thread):
                if self.terminal:
                    event = StopEvent
                else:
                    event = self.q.get()#key：该线程在这里继续等待新的任务，任务来了，继续执行
                                        #暂时将该线程对象放到free_list中。
        else:

            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，所有线程停止
        """
        self.cancel = True
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1

    def terminate(self):
        """
        无论是否还有任务，终止线程
        """
        self.terminal = True

        while self.generate_list:
            self.q.put(StopEvent)

        self.q.queue.clear()

    @contextlib.contextmanager
    def worker_state(self, free_list, worker_thread):
        """
        用于记录线程中正在等待的线程数
        """
        free_list.append(worker_thread)#新的任务来的时候判断
                                 # if len(self.free_list) == 0 and len(self.generate_list) < self.max_num
                                 # 任务得创建新的线程来处理；如果len(self.free_list) ！= 0：由阻塞着的存在free_list中的线程处理（event = self.q.get()）
        try:
            yield
        finally:
            free_list.remove(worker_thread)

# How to use


pool = ThreadPool(5)

def callback(status, result):
    # status, execute action status
    # result, execute action return value
    pass


def action(i):
    time.sleep(1)
    print(i)

for i in range(30):
    ret = pool.run(action, (i,), callback)

time.sleep(2)
print(len(pool.generate_list), len(pool.free_list))
print(len(pool.generate_list), len(pool.free_list))

# pool.close()
# pool.terminate()