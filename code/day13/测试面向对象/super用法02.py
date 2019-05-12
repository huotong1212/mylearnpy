class A():
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        # super(B, self).go()
        super().go() # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :**
        print ("go B go!")

a = A()
b = B()

b.go()