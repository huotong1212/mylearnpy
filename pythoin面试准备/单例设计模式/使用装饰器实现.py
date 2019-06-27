
def wrapper(cls):
    # instance = {}
    def inner(*args, **kwargs):
        if not hasattr(cls,'_instance'):
            # instance[cls] = cls(*args,**kwargs)
            cls._instance = cls(*args,**kwargs)
        # return instance[cls]
        return cls._instance
    return inner


@wrapper        # Singleton = wrapper(cls)
class Singleton(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

if __name__ == '__main__':
    s1 = Singleton(1,2)
    s2 = Singleton([],{})

    print(s1 == s2)
    print(s1 is s2)
    print(s1)
    print(s2)
    print(s1.a)
    print(s2.a)