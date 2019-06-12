class A():
    x = 7
    y = 8
    def __init__(self):
        self.z = 9
        self.n = 6
        print('A start........')
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    x = 6
    def __init__(self):
        self.n = 5
        print('B start........')
    def go(self):
        # super(B, self).go()
        super().go() # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :**
        print ("go B go!")

a = A()
print('---------')
b = B()

b.go()
print(a.n)
print(b.n)
print(a.x)
print(b.x)

print('-------')
print(b.y)
print(b.z)
