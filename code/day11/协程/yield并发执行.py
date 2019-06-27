
# #1 yiled可以保存状态，
# yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级


import time

def func1():
    time.sleep(1)
    while True:
        yield 1

def func2():
    for i in range(100):
        print(2)
        print(next(func1()))

start = time.time()
func2()
end = time.time()
print(end - start)