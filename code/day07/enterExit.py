
class Foo:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('执行了enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行了exit')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True  # 会捕获异常

with Foo('test') as f:
    print(f)
    print(wewqewq)  # 会直接触发exit
    print(f.name)