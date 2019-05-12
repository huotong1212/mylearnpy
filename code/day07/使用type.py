# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
#
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello1, %s.' % name)

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
h.hello()
print(type(Hello))
print(type(h))