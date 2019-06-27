class A(object):
    a1 = 'a1'

    def __init__(self):
        self.a2 = 'a2'
        self.a3 = 1


if __name__ == '__main__':
    aT1 = A()
    aT2 = A()

    print(aT1 == aT2)
    print(aT1 is aT2)

    print(aT1.a1 == aT2.a1)
    print(aT1.a1 is aT2.a1)

    print(aT1.a2 == aT2.a2)
    print(aT1.a2 is aT2.a2)

    print(aT1.a3 == aT2.a3)
    print(aT1.a3 is aT2.a3)

    aT1.b = 'b1'
    aT2.b = 'b1'

    print(aT1.b == aT2.b)
    print(aT1.b is aT2.b)

    aT1.c = []
    aT2.c = []

    print(aT1.c == aT2.c)
    print(aT1.c is aT2.c)

    aT1.d = str(1)
    aT2.d = str(1)

    print(aT1.d == aT2.d)
    print(aT1.d is aT2.d)

    # python中的字符串与java中的相似,会默认复用已经存在的字符串，他们的引用地址相同
    # 如果说我们自己手动创建的相同数值的字符串，那么不会复用，会指向不同的地址

    t1 = 'abc'
    t2 = 'abc'

    print(t1 == t2)
    print(t1 is t2)
