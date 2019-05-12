
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michel')
print(s())
print(callable(s)) # 被调用的对象就是一个Callable对象,可以被当作函数执行
print(callable('str'))