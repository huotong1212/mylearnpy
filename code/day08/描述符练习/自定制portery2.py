class myproperty(object):
    def __init__(self, func):
        print('init....')
        self.name = func.__name__

    def __get__(self, instance, owner):
        print('执行了get', instance, owner)
        # print('in dict',instance.__dict__)
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError(instance, 'object no attribute', self.name)
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('执行了set', instance, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('执行了delete')
        instance.__dict__.pop(self.name)

    def setter(self, func):
        print('执行了setter', func)
        return self

class People(object):
    # job = 6
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @property  # city = property(city)
    def city(self):
        return self.__city  # 报错，因为会无限递归，所以porperty中最好使用私有变量

    @city.setter  # city = property(city).setter
    def city(self, value):
        self.__city = value

    @myproperty  # job = myproperty(job)
    def job(self):
        return self.__job

    print(job) #myproperty对象 <__main__.myproperty object at 0x0000025C69B33550>
    @job.setter  # job = job<myproperty object>.setter(job)
    def job(self, value):
        print('set __ job')
        self.__job = value

    print('-----2',job) # <__main__.myproperty object at 0x00000244592C3B38>
    def xxx(self):
        return 1

    def xxx(self, value):
        return 2

    def __repr__(self):
        return str(self.__class__)

p1 = People('张三', 18, 2000.00)
# p1.city = '上海'
# print(p1.city)

# print(p1.xxx)
print(People.__dict__)
print(p1.__dict__)
# print(p1.job)  # 如果myproperty是只实现了get方法的非数据描述符，那么p1.job会找到下面重载的job函数（他会覆盖上面的job函数），他相当于类属性，但是实例也可以调用
# 如果把重载job函数注释掉，那么他就会找到这个非数据描述符，并执行其中的get方法,而且因为get中没有设置返回值，所有打印出来是None
# 如果把重载job函数注释掉,在描述符类中添加set那么就会找到这个优先级较高的描述符，并执行相应的方法
# 如果重载job函数,那么即使在描述符类中添加set，也只会找到job函数，因为类属性的优先级大于描述符,但是调用类的方法（）却是相当于调用非数据描述符
# 问题？如果说函数是非数据描述符的话，为什么这里的优先级会比数据描述符大呢
# 不管了，反正只要不同名就行了
# print(p1.xxx())
# print(p1.xxx(2))
p1.job = 'dsa'
print('p1-------',p1.job)
print('People------',People.job)
print(p1.__dict__)
print(People.__dict__)