# python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法
# set、wait、clear。
#
# 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为
# False，那么当程序执行
# event.wait
# 方法时就会阻塞，如果“Flag”值为True，那么event.wait
# 方法时便不再阻塞。
#
# clear：将“Flag”设置为False
# set：将“Flag”设置为True

# _*_coding:utf-8_*_
# !/usr/bin/env python

from multiprocessing import Process, Event
import time, random


def car(e, n):
    while True:
        if not e.is_set():  # Flase
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait()
            print('\033[32m车%s 看见绿灯亮了\033[0m' % n)
            time.sleep(random.randint(3, 6))
            if not e.is_set():
                continue
            print('走你,car', n)
            break


def police_car(e, n):
    while True:
        if not e.is_set():
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait(1)
            print('灯的是%s，警车走了,car %s' % (e.is_set(), n))
            break


def traffic_lights(e, inverval):
    while True:
        time.sleep(inverval)
        if e.is_set():
            e.clear()  # e.is_set() ---->False
        else:
            e.set()


if __name__ == '__main__':
    e = Event()
    # for i in range(10):
    #     p=Process(target=car,args=(e,i,))
    #     p.start()

    for i in range(5):
        p = Process(target=police_car, args=(e, i,))
        p.start()
    t = Process(target=traffic_lights, args=(e, 10))
    t.start()

    print('============》')

# Event（同线程一样）