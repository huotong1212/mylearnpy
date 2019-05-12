
class Foo:
    def __get__(self, instance, owner):
        print('执行Foo get')
    def __set__(self, instance, value):
        print('执行Foo set')
        print('----',instance,value)
    def __delete__(self, instance):
        print('执行Foo del')

class Skt:
    x = Foo()
    def __init__(self,n):
        self.x = n

s = Skt(10)

s.x
s.x = 12
del s.x
