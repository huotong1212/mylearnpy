
class People(object):
    name = 5
    age = 6
    def name(self):
        print('self name')

p1 = People()
print(People.__dict__)
print(p1.name)
print(p1.__dict__)
print(hasattr(People.name,'__set__'))
print(hasattr(People.name,'__get__'))
print(hasattr(People.name,'__delete__'))
print(hasattr(People.age,'__set__'))
print(hasattr(People.age,'__get__'))
print(hasattr(People.age,'__delete__'))

# 结论，经过测试发现，当方法和类属性同名时，谁后编译就保留谁，
# 所有他们的优先级相同，而且他们都不是实例属性