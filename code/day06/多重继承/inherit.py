from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 功能
class Runnable(object):
    def run(self):
        print('Running......')

class Flyable(object):
    def fly(self):
        print('Flying.......')

# 细分
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

# 编写一个多进程模式的TCP服务，定义如下
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 编写一个多线程模式的UDP服务，定义如下
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。