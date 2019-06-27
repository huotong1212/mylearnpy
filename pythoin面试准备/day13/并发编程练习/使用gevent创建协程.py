
import gevent
from gevent import monkey;monkey.patch_all()
import time

def func1(name):
    print(f'{name} func1 start......')
    time.sleep(2)
    print(f'{name} func1 end......')

def func2(name):
    print(f'{name} func2 start......')
    time.sleep(3)
    print(f'{name} func2 end......')

g1 = gevent.spawn(func1,'小明')
g2 = gevent.spawn(func2,'Mitchell')

g1.join()
g2.join()

# gevent.joinall([g1,g2])
print('Main Thread end...')

