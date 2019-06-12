'''
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

#疑问:如果我用类名去操作属性呢
People.name #报错,错误的根源在于类去操作属性时,会把None传给instance
'''

#修订__get__方法
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    # def __set__(self, instance, value):
    #     print('set--->',instance,value)
    #     instance.__dict__[self.name]=value
    # def __delete__(self, instance):
    #     print('delete--->',instance)
    #     instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

# print(People.name) #完美,解决

p1 = People('張三',12,321) # 这段代码可以证明实例属性的优先级大于只实现了get方法的非数据描述符
print(p1.name)
print(p1.__dict__)