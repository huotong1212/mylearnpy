def ATest(a, b=[1,]):
    c = {}
    print(a)
    print(b)
    print(c)

class A(object):
    def __init__(self,a, b=[1,]):
        c = {}
        print(a)
        print(b)
        print(c)

if __name__ == '__main__':
    ATest(1, [3, 5])
    # ATest.c['c1'] = 'jack'
    ATest(2, ['a', 'b'])
    # ATest.c['c2'] = 'tom'
    ATest(3, ['c', 'd'])
