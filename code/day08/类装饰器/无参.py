def decorate(cls):
    print('类的装饰器开始运行啦------>')
    return cls

@decorate #无参:People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3333.3)

