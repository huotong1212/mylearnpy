class Foo:
    def func(self):
        print('我胡汉三又回来了')

    def __getattr__(self, item):
        print('找不到了当然是来找我啦',item)
f1=Foo()

f1.xxxxxxxxxxx