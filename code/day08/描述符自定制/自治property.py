
##自治property
class Lazyproperty:
    def __init__(self,func):
        self.func = func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.test实际是要执行r1.test()')
        if instance is None:
            return self
        return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情,是get方法中的instance

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @property  # area = property(area)
    def area(self):
        return self.width * self.length

    @Lazyproperty   # test = Lazyproperty(test)  这一步实例化了lazyproperty对象，并将test函数赋值给了func
    def test(self):
        return self.width + self.length

r1=Room('alex',2,3)
print(r1.area)