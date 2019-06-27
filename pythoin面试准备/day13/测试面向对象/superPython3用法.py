class A():
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super().go()
        print ("go B go!")
class C(A):
    def go(self):
        super().go()
        print ("go C go!")
    def stop(self):
        super().stop()
        print ("stop C stop!")
class E(A):
    def go(self):
        super().go()
        print ("go E go!")
    def stop(self):
        super().stop()
        print ("stop E stop!")

class D(B,C,E):
    def go(self):
        super().go()
        print ("go D go!")
    def stop(self):
        super().stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()
print('--------')
b.go()
print('--------')
c.go()
print('--------')
d.go()
print('--------')
e.go()
print('--------')
a.stop()
print('--------')
b.stop()
print('--------')
c.stop()
print('--------')
d.stop()
print('--------')
e.stop()
print(D.mro())
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()