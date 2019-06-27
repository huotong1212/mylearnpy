class A(object):
    def __init__(self, *args, **kwargs):
        print("init A")

    def __new__(cls, *args, **kwargs):
        print("new A %s" % cls)
        # return super(A, cls).__new__(cls, *args, **kwargs)
        return object.__new__(cls, *args, **kwargs)


class B(A):
    def __init__(self, *args, **kwargs):
        print("init B")

    def __new__(cls, *args, **kwargs):
        print("new B %s" % cls)
        return super(B, cls).__new__(cls, *args, **kwargs)
        #return object.__new__(cls, *args, **kwargs)

if __name__ == "__main__":
    a = A()
    b = B()
