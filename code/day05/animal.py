
### 演示继承和多态

class Animal(object):
    def __init__(self):
        self.run()

    def run(self):
        print('this animal is running,it\'s %s'%(self))


class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Dog is eating')
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('Cat is eating')
    pass

if __name__ == '__main__':
    a = Animal()
    # a.run()

    dog = Dog()
    # dog.run()

    cat = Cat()
    # cat.run()

class Timer(object):
    def run(self):
        print('Start...')

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
# 否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    print()
    # run_twice(Dog())
    # run_twice(Cat())
    # run_twice(Timer())