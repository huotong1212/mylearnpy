





class People(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        print('get,self,age')
        return self.__age

    @age.setter
    def age(self,value):
        print('set,self,age')
        self.__age = value

p1 = People('小明',20)
print(p1.age)
p1.age = 16
print(p1.age)