#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

class People(object):
    name=Str()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age

    def name(self):
        print('get name')

p1=People('egon',18)# 得出结论，如果我们在使用对象调用name时，碰巧他是类属性或者方法，
                    # 那么name将会做完这个实例的实例属性
print(p1.name)
