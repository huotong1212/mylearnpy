
class myproperty(object):
    def __init__(self,func):
        print('init....')
        self.func = func

    def __get__(self,instance,owner):
        print('执行了get',instance,owner)
        if instance is None:
            return self
        return 'get'

    def __set__(self,instance,value):
        print('执行了set',instance,value)

    def __delete__(self,instance):
        print('执行了delete')
        instance.__dict__.pop(self.name)

    def setter(self,instance,value):
        print('执行了set', instance, value)


class People(object):
    # job = 6
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    @property  # city = property(city)
    def city(self):
        return self.__city  # 报错，因为会无限递归，所以porperty中最好使用私有变量

    @city.setter  # property(city).setter
    def city(self,value):
        self.__city = value

    @myproperty  # job = myproperty(job)
    def job(self):
        return self.__job

    @job.setter # myproperty(job).setter
    def job(self,value):
        print('set job')
        self.__job = value

    def xxx(self):
        return 1

    def xxx(self,value):
        return 2

p1 = People('张三',18,2000.00)
# p1.city = '上海'
# print(p1.city)

# print(p1.xxx)
print(People.__dict__)

print(p1.job) # 如果myproperty是只实现了get方法的非数据描述符，那么p1.job会找到下面重载的job函数（他会覆盖上面的job函数），他相当于类属性，但是实例也可以调用
                # 如果把重载job函数注释掉，那么他就会找到这个非数据描述符，并执行其中的get方法,而且因为get中没有设置返回值，所有打印出来是None
                # 如果把重载job函数注释掉,在描述符类中添加set那么就会找到这个优先级较高的描述符，并执行相应的方法
                # 如果重载job函数,那么即使在描述符类中添加set，也只会找到job函数，因为类属性的优先级大于描述符,但是调用类的方法（）却是相当于调用非数据描述符
                # 问题？如果说函数是非数据描述符的话，为什么这里的优先级会比数据描述符大呢
                # 不管了，反正只要不同名就行了
# print(p1.xxx())
# print(p1.xxx(2))
print(p1.__dict__)
print(People.__dict__)