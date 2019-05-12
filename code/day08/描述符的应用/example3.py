class Str:
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
        if not isinstance(value,self.expected_type): #如果不是期望的类型，则抛出异常
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name',str) #新增类型限制str
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)#传入的name因不是字符串类型而抛出异常

