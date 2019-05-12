
import time
import functools

def timmer(func):
    @functools.wraps(func)  #保持函数签名一致 wrapper.__name__ = func.__name__
    def wrapper(*args,**kwargs):
        print(args)
        for a,b in (kwargs.items()):
            print(a,b)
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("运行时间为%s"%(end_time-start_time))
        return res
    return wrapper

@timmer
def cop(a,b):
    time.sleep(3)
    print("test测试函数运行完毕......")

cop(a=2,b=3)  #这里运行的其实就是wrapper