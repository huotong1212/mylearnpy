
class LazyStaticmethod:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        def feedback(*args,**kwargs):
            print('----Get--FeedBack')
            self.func(*args,**kwargs)
        return feedback
class Foo:
    @staticmethod #装饰器
    def spam(x,y,z):
        print(x,y,z)

    def spam2(x,y,z):
        print(z,y,x)

    @LazyStaticmethod # spam3 = LazyStaticmethod(spam3)
    def spam3(x,y,z):
        print(z,y,x)
Foo.spam2(1,2,3)
f1 = Foo()
# f1.spam2(2,3,4)
print('-'*20)
Foo.spam3(5,6,7)
f2 = Foo()
f2.spam3(7,8,9)