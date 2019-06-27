import functools
import time

def computeTime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        perform_time = start-end
        print(perform_time)
        return result
    return wrapper



@computeTime
def A(a,b, **obj):
    print('A ..........')
    print(a,b)
    time.sleep(1)
    print(obj)
    return a+b

obj = {'c':1,'d':2}
print(A(1,3,**obj))