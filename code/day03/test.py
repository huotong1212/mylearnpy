def lazy_sum(*args):
    b = 0
    def sum():
        ax = 0
        print('b:',b)
        for n in args:
            ax = ax + n
        return ax
    return sum

# b = 1
#
# func = lazy_sum(1,2)
# print(func)
# print(type(func))
# num = func()
# print('num:',num)


class Test:
    b = 2

    def __init__(self):
        self.b = 3

    @staticmethod
    def lazy_sum(*args): # 默认的*args，使用对象调用会传入Test类对象，因此需要加上注解Staticmethod，
                        # 使其不要传入self对象,或者使用类直接调用方法
        b = 6
        print('locals:',locals())
        def sum():
            ax = 0
            print('b:', b)
            # print('selfb:',self.b)
            print('args:',args)
            for n in args:
                ax = ax + n
            return ax

        return sum

b = 1

# t = Test()
# fun = t.lazy_sum(1,2)
fun = Test.lazy_sum(2,3)
print(fun)
print(type(fun))
fun()