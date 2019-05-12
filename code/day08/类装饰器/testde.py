
## 描述符类，用于代理类中的属性
class Typed:
    def __init__(self,name,except_type):
        self.name = name
        self.except_type = except_type

    def __get__(self, instance, owner):
        print('执行了get')
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('执行了set')
        if isinstance(value,self.except_type):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('输入值类型错误')

    def __delete__(self, instance):
        print('执行了delete')

def typeassert(**kwargs):
    def wrapper(cls):
        print('装饰器只运行了一次')  ## Hip = wrapper(Hip)
        for key,value in kwargs.items():
            setattr(cls,key,Typed(key,value))  ### 给类设置类属性
            print('---',cls.__dict__)
        return cls
    return  wrapper

@typeassert(name=str,age=int,salary=float)
class Hip():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

h = Hip('Mike',18,1235.66)
print(h.name)
# h.name = 2312
h.name = 'Keiven'
print(h.name)
print(h.__dict__)
print(Hip.__dict__)