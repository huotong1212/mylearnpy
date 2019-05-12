
### 闭包
def add_wrapper(a,b):
    def add():
        return a+b
    return add

f = add_wrapper(1,2)
print(type(f))
print(f())

### 装饰器=高阶函数+函数嵌套+闭包
import time



### 装饰器
def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间是%s秒"%(end_time - start_time))
        return  end_time - start_time
    return wrapper

# print(timmer(test)())
# test = timmer(test)
# test()
# 不修改被修饰函数的源代码
# 不修改被装饰函数的调用方式

# @timmer 就相当于 test = timmer(test)

@timmer
def hop():
    time.sleep(3)
    print("test测试函数运行完毕......")

hop()