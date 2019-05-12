# 一 描述符本身应该定义成新式类,被代理的类也应该是新式类
# 二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 三 要严格遵循该优先级,优先级由高到底分别是
# 1.类属性
# 2.数据描述符
# 3.实例属性
# 4.非数据描述符
# 5.找不到的属性触发__getattr__()

class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Typed('name',str)
    age=Typed('name',int)
    salary=Typed('name',float)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)
p1=People('egon','18',3333.3)
p1=People('egon',18,3333)

