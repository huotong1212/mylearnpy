class A(object):
    a_1 = 'a1'

    def __init__(self):
        self.a_2 = 'a2'


class B(A):
    b_1 = 'b1'
    # b_4 = super() super必须要传self
    # b_4 = super().__new__(super().__class__)

    def __init__(self):
        self.b_2 = 'b2'
        self.b_3 = super().__new__(self.__class__)


class C(B):
    c_1 = 'c1'

    def __init__(self):
        self.c_2 = 'c2'


if __name__ == '__main__':
    aT = A()
    aG = A()
    bT = B()
    cT = C()

    print(aT.__dict__)
    print(A.__dict__)
    print(bT.__dict__)
    print(B.__dict__)
    print(cT.__dict__)
    print(C.__dict__)

    print('-'*20)
    print(C.b_1) # C中可以调用B中的类属性，但不会存放到C中的dict中去