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

# p1=People('egon',18)
#
# #如果描述符是一个数据描述符(即有__get__又有__set__),那么p1.name的调用与赋值都是触发描述符的操作,于p1本身无关了,相当于覆盖了实例的属性
# p1.name='egonnnnnn'
# p1.name
# print(p1.__dict__)#实例的属性字典中没有name,因为name是一个数据描述符,优先级高于实例属性,查看/赋值/删除都是跟描述符有关,与实例无关了
# del p1.name

p1=People('egon',18)# 得出结论，如果我们在使用对象调用name时，碰巧他是类属性或者方法，
                    # 那么name将会做完这个实例的实例属性
print(p1.name)
print(People.name)
People.name = 'alex'# 得出结论，如果使用类调用name的话，那么他将会以类属性的形式存在，所有类属性的优先级大于数据描述符
print(People.name)