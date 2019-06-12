
class myclassmethod(object):
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        def inner(*args, **kwargs):
            result = self.func(owner,*args,**kwargs)
            return result
        return inner

    def __set__(self, instance, value):
        pass

class mystaticmethod(object):
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        def inner(*args,**kwargs):
            result = self.func(*args,**kwargs)
            return result
        return inner

    def __set__(self, instance, value):
        pass

class People(object):
    job = 'cooker'

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def achievejob(cls,name):
        return name+cls.job

    @myclassmethod  # obtainjob = myclassmethod(obtainjob)
    def obtainjob(cls,name):
        return name+cls.job

    @staticmethod
    def gainAdress(city):
        return 'live in'+city

    @mystaticmethod
    def getAdress(city):
        return 'live in'+city


p1 = People('李白',20,66666.66)
print(p1.achievejob('tom')) # tomcooker
print(People.achievejob('tom')) # tomcooker

print(p1.obtainjob('faker')) # fakercooker
print(People.obtainjob('faker')) # fakercooker

print(p1.gainAdress('成都')) # live in成都
print(People.gainAdress('成都')) # live in成都

print(p1.getAdress('常州')) # live in常州
print(People.getAdress('常州')) # live in常州