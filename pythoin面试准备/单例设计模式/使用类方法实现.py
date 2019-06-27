import threading
import time


class SingleTon(object):
    lock = threading.Lock()
    def __init__(self,i):
        time.sleep(1)
        pass

    @classmethod
    def instance(cls,*args, **kwargs):
        if not hasattr(cls,'_instance'):
            with SingleTon.lock: #为了保证线程安全在内部加锁
                if not hasattr(cls, '_instance'):
                    cls._instance = cls(*args, ** kwargs)
        return cls._instance

if __name__ == '__main__':
    for i in range(1,10):
        t = threading.Thread(target = lambda i :print(SingleTon(i)),args = (i, ))
        print('t:',t)
        t.start()